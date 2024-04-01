# SPDX-License-Identifier: Apache-2.0

SIM=icarus

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/../../../verilog/AsyncQueue.v

TOPLEVEL := AsyncQueue
MODULE   := test_asyncfifo

include $(shell cocotb-config --makefiles)/Makefile.sim
