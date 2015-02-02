import ctypes as c

class TX_SYSTEMCOMPONENTOVERRIDEFLAGS():
    TX_SYSTEMCOMPONENTOVERRIDEFLAG_NONE = 0
    TX_SYSTEMCOMPONENTOVERRIDEFLAG_MEMORYMODEL = 1 << 0,
    TX_SYSTEMCOMPONENTOVERRIDEFLAG_THREADINGMODEL = 1 << 1,
    TX_SYSTEMCOMPONENTOVERRIDEFLAG_LOGGINGMODEL = 1 << 2,
    TX_SYSTEMCOMPONENTOVERRIDEFLAG_SCHEDULINGMODEL = 1 << 3


TX_TRUE = 1
TX_FALSE = 0

TX_RESULT_OK = 2

TX_GAZEPOINTDATAMODE_LIGHTLYFILTERED = 2


class TX_GAZEPOINTDATAPARAMS(c.Structure):
    _fields_ = [("GazePointDataMode", c.c_int),
    ]


class TX_GAZEPOINTDATAEVENTPARAMS(c.Structure):
    _fields_ = [("GazePointDataMode", c.c_int),
                ("timestamp", c.c_double),
                ("x", c.c_double),
                ("y", c.c_double),
    ]


EVENT_HANDLER = c.CFUNCTYPE(None, c.c_void_p, c.c_void_p)
ON_SNAPSHOT_COMMITTED = c.CFUNCTYPE(None, c.c_void_p, c.c_void_p)
CONNECTION_HANDLER = c.CFUNCTYPE(None, c.c_int, c.c_void_p)