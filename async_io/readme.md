# async_io

#### reason  

* **In python , Cpu run faster than I/O.I/O spend more time.General,I/O will block the process.So ,I can use threading or multiprocessing , this is the one ideal , the other idael is to use asynchronous i/o like javascript's asynchronous , this means if I met asynchronous , the process would continue run , till get i/o result would execute the callback**