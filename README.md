# Asynchronous FIFO
This repo contains an asynchronous FIFO. Source code has been modified from rocket-chip project. Original source code can be found here: https://github.com/chipsalliance/rocket-chip/blob/master/src/main/scala/util/AsyncQueue.scala .
## Usage
Instantiate it in your code like this:
```scala
val fifoparams = AsyncQueueParams(
    depth = 8,
    sync = 3,
    safe = false,
    narrow = false
)
val asyncfifo = Module(new AsynqQueue(UInt(32.W), fifoParams))
```
## Parameters
There are five parameters:
- `T` - the data type of one FIFO entry. `UInt(32.W)` in the example above.
- `depth` - this decides the depth of the FIFO, i.e. how many entries of `T` is included
- `sync` - number of synchronization registers used in clock domain crossing. Must be at least 2.
- `safe` - setting this `true` allows separately resetting one clock domain (when the fifo is empty), while the other clock domain is not reset. It adds logic to synchronize read and write indices. If set to false, both domains need to be reset at the same time.
- `narrow` - when `true`, moves read mux from sink side to source side. Increases combinational path, but reduces the number of level shifters needed if clock crossing is also a voltage crossing.
## IOs
- `io.enq_clock` - input, clock signal, source side
- `io.enq_reset` - input, asynchronous reset, source side
- `io.enq` - bundle, data, source side
  - `.bits` - input, data
  - `.valid` - input, data is valid
  - `.ready` - output, source is ready to accept data
- `io.deq_clock` - input, clock signal, sink side
- `io.deq_reset` - input, asynchronous reset, sink side
- `io.deq` - bundle, data, sink side
  - `.bits` - output, data
  - `.valid` - output, data is valid
  - `.ready` - input, sink is ready to accept data
## Generate Verilog
```
./configure && make TestAsyncQueue
```
Generates verilog under `verilog/` folder. The parameters are `T = UInt(32.W)`, `depth = 8`, `sync = 3`, `safe = false`, `narrow = false`. The parameters can be changed by modifying them in the class instantiation located in `AsyncQueue.scala` (find an object called `TestAsyncQueue`).
## Test
A test in `src/main/test/cocotb` instantiates two different clocks for the async FIFO. Then, it generates data values from 0 to 99, sends them to the FIFO, and monitors the outputs.

The test can be run by navigating to the path above and running `make`.
