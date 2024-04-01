# SPDX-License-Identifier: Apache-2.0

# for list type hints
from __future__ import annotations

# pip install cocotb
import cocotb
import random
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, with_timeout, RisingEdge

# pip install cocotbext-axi
from cocotbext.axi import AxiLiteBus, AxiLiteRam, AxiLiteMaster

@cocotb.test()
async def test_asyncfifo(dut):
    """
    Testing asynchronous FIFO
    """
    source_clock = dut.io_enq_clock
    source_reset = dut.io_enq_reset
    sink_clock = dut.io_deq_clock
    sink_reset = dut.io_deq_reset

    source_reset.value = 0
    sink_reset.value = 0

    dut.io_enq_valid.value = 0
    dut.io_enq_bits.value = 0
    dut.io_deq_ready.value = 1

    cocotb.start_soon(Clock(source_clock, 10, units="step").start())
    cocotb.start_soon(Clock(sink_clock, 6, units="step").start())

    await RisingEdge(source_clock)
    source_reset.value = 1
    sink_reset.value = 1
    await ClockCycles(source_clock, 10)
    source_reset.value = 0
    sink_reset.value = 0

    dut.io_enq_bits.value = 0
    dut.io_enq_valid.value = 1
    for i in range(1, 100):
        await RisingEdge(source_clock)
        while True:
            if (dut.io_enq_ready.value == 1):
                dut.io_enq_bits.value = i
                break
            else:
                await RisingEdge(source_clock)


