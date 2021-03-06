##
##

import argparse
import sys

from dynamicserialize.dstypes.com.raytheon.uf.common.dataplugin.gfe.db.objects import DatabaseID
from dynamicserialize.dstypes.com.raytheon.uf.common.dataplugin.gfe.db.objects import ParmID


class UsageArgumentParser(argparse.ArgumentParser):
    """
    A subclass of ArgumentParser that overrides error() to print the
    whole help text, rather than just the usage string.
    """
    def error(self, message):
        sys.stderr.write('%s: error: %s\n' % (self.prog, message))
        self.print_help()
        sys.exit(2)

## Custom actions for ArgumentParser objects ##
class StoreDatabaseIDAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        did = DatabaseID(values)
        if did.isValid():
            setattr(namespace, self.dest, did)
        else:
            parser.error("DatabaseID [" + values + "] not a valid identifier")

class AppendParmNameAndLevelAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        tx = ParmID.parmNameAndLevel(values)
        comp = tx[0] + '_' + tx[1]
        if (hasattr(namespace, self.dest)) and \
            (getattr(namespace, self.dest) is not None):
                currentValues = getattr(namespace, self.dest)
                currentValues.append(comp)
                setattr(namespace, self.dest, currentValues)
        else:
            setattr(namespace, self.dest, [comp])

