from argparse import ArgumentParser
import socket
from threading import Thread
from time import time

open_port=[]
def prepare_args():
    """
    Prepare Arguments
    return args (argparse.Namespace)
    """
    parser = ArgumentParser(
        description="Python Port Scanner",
        usage="%(prog)s 192.168.1.2",
        epilog="Example - %(prog)s -s 20 -e 40000 -t 500 -V 192.168.1.2"
    )
    parser.add_argument(metavar='IPv4', dest='ip', help="host to scan")
    parser.add_argument("-s", '--start', dest="start", type=int, help="starting port", default=1,metavar="")
    parser.add_argument('-e', '--end', dest="end", type=int, help="ending port", default=65535,metavar="")
    parser.add_argument('-t', '--threads', dest="threads", type=int, help="threads to use", default=500,metavar="")
    parser.add_argument('-V', "--verbose", dest="verbose", action='store_true', help='verbose output')
    parser.add_argument('-v', "--version", action='version', version='%(prog)s 1.0')

    args = parser.parse_args()
    return args

def prepare_ports(start:int,end:int):
    """
    Generator function for ports generating 
    arguements:
        start(int) - starting port
        end(int) - ending port
    """
    for port in range(start,end+1):
        yield port

def scan_port():
    """scan ports
    """
    while(1):
        try:
            s=socket.socket()
            s.settimeout(1)
            port=next(ports)
            s.connect((arguments.ip,port))
            open_port.append(port)
            if arguments.verbose:
                print(f"\r{open_port}",end="")
        except (ConnectionRefusedError,socket.timeout):
            continue
        except StopIteration:
            break


def prepare_threads(threads:int):
    """create,start,join threads
    arguements:
        threads(int) - Number of threads to use
    """
    thread_list=[]
    for i in range(threads+1):
        thread_list.append(Thread(target=scan_port))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    arguments = prepare_args()
    ports=prepare_ports(arguments.start,arguments.end)
    start_time=time()
    prepare_threads(arguments.threads)
    end_time=time()
    if arguments.verbose:
        print()
    print(f"Open Ports Found - {open_port}")
    print(f"Time taken - {round(end_time-start_time,2)} sec")