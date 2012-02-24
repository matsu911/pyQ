from struct import *

def get_result(host, port, query):
    handle = libk.khpu(host, port, "")

    result = libk.k(handle, query, 0)

    if not result:
        raise "Network Error"

    if result.type() == -128:
        libk.kclose(handle)
        raise "Server Error %s" % str(result)

    libk.kclose(handle)

    if result.type() != 99 and result.type() != 98:
        # accept table or dict
        libk.r0(result)
        raise "type %d\n" % result.type()

    flip = libk.ktd(result) # if keyed table, unkey it. ktd decrements ref count of arg. 

    columnNames = cast(flip.contents.union.k, K)[0]
    columnData  = cast(flip.contents.union.k, K)[1]

    header = map(converter(columnNames.type()), columnNames)
    data   = [ map(converter(x.type()), x) for x in columnData]
    libk.r0(flip)
    return header, zip(*data)
