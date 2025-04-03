import sys
sys.path.append('.')
import src.demo as demo

assert demo.print_hello_world() == "Hello World", "Function did not return expected value"