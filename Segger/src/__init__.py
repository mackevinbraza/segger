from chimerax.core.toolshed import BundleAPI

class _SeggerAPI(BundleAPI):
    @staticmethod
    def initialize(session, bundle_info):
        """Register file formats, commands, and database fetch."""
        from .segfile import register_segmentation_file_format
        register_segmentation_file_format(session)

    @staticmethod
    def start_tool(session, tool_name):
        if tool_name == 'Segment Map':
            from .segment_dialog import Volume_Segmentation_Dialog
            d = Volume_Segmentation_Dialog.get_singleton(session)
        elif tool_name == 'Fit to Segments':
            from .fit_dialog import Fit_Segments_Dialog
            d = Fit_Segments_Dialog.get_singleton(session)
        return d

    @staticmethod
    def register_command(command_name, logger):
        # 'register_command' is lazily called when the command is referenced
        from . import segcmd
        segcmd.register_segger_command(logger)

bundle_api = _SeggerAPI()

# ------------------------------------------------------------------------------
#
dev_menus = False       # Include under-development menus.
timing = False          # Report execution times for optimizing code.
seggerVersion = '2.3'
debug = False		# Whether to output debugging messages

from .regions import Segmentation, Region, SelectedRegions
