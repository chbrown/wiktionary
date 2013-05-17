from cStringIO import StringIO


def chunker(lines, start, end):
    buf = StringIO()
    inside = False

    for line in lines:
        if not inside and line == start:
            inside = True

        if inside:
            buf.write(line)

        if inside and line == end:
            inside = False
            # flush
            buf.seek(0)
            yield buf.read()
            buf.truncate(0)

    # we ignore un-ended final chunks
