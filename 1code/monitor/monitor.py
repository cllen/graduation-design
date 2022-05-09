#!/usr/bin/python


 
import sys
import time
import psutil

import asyncio

seconds = 60*1
interval = 1 # polling seconds


files = []

pids = []

async def watch(pid):
    
    times = int(seconds/interval)

    pid = int(pid)
    p = psutil.Process(pid)
    # monitor process and write data to file
    filename = "process_monitor_" + p.name() + '_' + str(pid) + ".csv"
    files.append(filename)
    with open(filename, "w+") as f:
        f.write("time,cpu%,mem%\n") # titles
        for i in range(times):
            # current_time = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            cpu_percent = p.cpu_percent() # better set interval second to calculate like:  p.cpu_percent(interval=0.5)
            mem_percent = p.memory_percent()
            line = current_time + ',' + str(cpu_percent) + ',' + str(mem_percent)
            print (pid,line)
            f.write(line + "\n")
            await asyncio.sleep(interval)

async def main():
    results = []
    files = []
    for pid in pids:
        print('watching {}...'.format(pid))
        result = asyncio.ensure_future(watch(pid))
        results.append(result)
    
    while False in [result.done() for result in results]:
        await asyncio.sleep(1)


if __name__ == '__main__':

    # get pid from args
    if len(sys.argv) < 2:
        print ("missing pid arg")
        sys.exit()


    pids = sys.argv[2:]

    seconds = int(sys.argv[1])

    try:
        print('watching pids:{}...'.format(pids))
        loop = asyncio.get_event_loop()    
        loop.run_until_complete(main())
    finally:
        print('done.')
        loop.close()


    # 打开这些文件
    def sumup(files):

        import csv

        totals = []
        for filename in files:
            f = csv.reader(open(filename,'r'))
            for index,raw in enumerate(f):
                if index == 0:
                    if len(totals) ==0:
                        totals.append(raw)
                    continue

                while len(totals) < index+1:
                    totals.append([0,0,0])


                totals[index][0] = raw[0]
                totals[index][1] = float(totals[index][1]) + float(raw[1])
                totals[index][2] = float(totals[index][2]) + float(raw[2])

        with open('process_monitor_total.csv', "w+") as f:
            for raw in totals:
                line = raw[0] + ',' + str(raw[1]) + ',' + str(raw[2])
                f.write(line + "\n")
                # print(line)


    sumup(files)