# SPDX-License-Identifier: Apache-2.0

SIM=icarus

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/../../../verilog/AsyncQueue.v

TOPLEVEL := AsyncQueue
MODULE   := test_asyncfifo

include $(shell cocotb-config --makefiles)/Makefile.sim

%.v: clean_vlog
	cd $(PWD)/../../.. && ./configure && $(MAKE) TestAsyncQueue

clean_vlog:
	rm -f $(VERILOG_SOURCES)

