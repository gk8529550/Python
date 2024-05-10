# import argparse
# import requests
# parser=argparse.ArgumentParser()
# parser.add_argument("url",help="https://www.investopedia.com/thmb/L5ff_qFD8KFPz1_bziiGCCi6bec=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/EulersNumber3-2-d37c1c359b704e9da734acd5517cd0a0.jpg")
# parser.add_argument("output",help="e value")
# args=parser.parse_args()
# print(args.arg1)
# print(args.arg2)

import argparse
parser = argparse.ArgumentParser(description ='Process some integers.')
parser.add_argument('integers', metavar ='N', 
					type = int, nargs ='+',
					help ='an integer for the accumulator')

parser.add_argument(dest ='accumulate', 
					action ='store_const',
					const = sum, 
					help ='sum the integers')

args = parser.parse_args()
print(args.accumulate(args.integers))
