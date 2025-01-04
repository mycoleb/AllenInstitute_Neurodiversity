# src/analysis/neuron_types.py

import pandas as pd
import numpy as np

class NeuronAnalyzer:
    def __init__(self):
        """Initialize the neuron analyzer"""
        pass
    
    def analyze_distribution(self, neuron_data):
        """
        Analyze the distribution of neuron types
        
        Args:
            neuron_data (pd.DataFrame): DataFrame containing neuron data
            
        Returns:
            dict: Analysis results including distributions and statistics
        """
        results = {
            'data': neuron_data,
            'total_count': len(neuron_data),
            'summary_stats': self._calculate_summary_stats(neuron_data)
        }
        
        return results
    
    def _calculate_summary_stats(self, data):
        """Calculate summary statistics for neuron data"""
        stats = {
            'count': len(data),
            'mean': data.mean(numeric_only=True).to_dict(),
            'std': data.std(numeric_only=True).to_dict()
        }
        return stats