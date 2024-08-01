import sys
import traceback
from variables import PROGRAM_INFO
from program_loop import Program

try:
	program = Program(PROGRAM_INFO)
	program.main_loop()
except Exception:
	traceback.print_exc()
	sys.exit()