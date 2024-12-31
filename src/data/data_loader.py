# src/data/data_loader.py

from allensdk.core.mouse_connectivity_cache import MouseConnectivityCache
from allensdk.api.queries.mouse_connectivity_api import MouseConnectivityApi
import pandas as pd

class BrainDataLoader:
    def __init__(self):
        """Initialize connections to Allen Brain Atlas API"""
        self.mcc = MouseConnectivityCache()
        self.mcapi = MouseConnectivityApi()
        self.structure_tree = self.mcc.get_structure_tree()
    
    def get_brain_regions(self):
        """Get all brain regions from the atlas"""
        regions = self.structure_tree.get_structures_with_properties()
        return pd.DataFrame(regions)
    
    def get_neuron_data(self, structure_id=None):
        """Get neuron data for a specific brain structure"""
        cells = self.mcapi.get_cell_types(structure_id) if structure_id else self.mcapi.get_cell_types()
        return pd.DataFrame(cells)
    
    def get_connectivity_data(self, structure_id):
        """Get connectivity data for a specific brain structure"""
        return self.mcapi.get_structure_connectivity(structure_id)