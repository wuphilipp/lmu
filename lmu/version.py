name = "lmu"
version_info = (0, 1, 0)  # (major, minor, patch)
dev = 0

version = "{v}{dev}".format(
    v=".".join(str(v) for v in version_info),
    dev=(".dev%d" % dev) if dev is not None else "",
)
