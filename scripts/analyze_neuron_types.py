# scripts/analyze_neuron_types.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data.data_loader import BrainDataLoader
from src.analysis.neuron_types import NeuronAnalyzer
from src.visualization.plotters import NeuronPlotter
import argparse

def main():
    print("Starting neuron analysis...")
    
    parser = argparse.ArgumentParser(description='Analyze neuron types in brain regions')
    parser.add_argument('--region-id', type=int, help='ID of brain region to analyze')
    parser.add_argument('--output-dir', type=str, default='output', help='Directory for output files')
    args = parser.parse_args()

    print(f"Initializing components...")
    # Initialize components
    loader = BrainDataLoader()
    analyzer = NeuronAnalyzer()
    plotter = NeuronPlotter()

    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    print(f"Output directory created/verified: {args.output_dir}")

    # Get data
    print("Fetching data from Allen Brain Atlas...")
    if args.region_id:
        print(f"Analyzing specific region ID: {args.region_id}")
        neuron_data = loader.get_neuron_data(args.region_id)
    else:
        print("Analyzing all regions")
        neuron_data = loader.get_neuron_data()
    
    print(f"Data shape: {neuron_data.shape if hasattr(neuron_data, 'shape') else 'No data returned'}")
    print("Sample of retrieved data:")
    print(neuron_data.head() if hasattr(neuron_data, 'head') else neuron_data)

    # Analyze data
    print("\nAnalyzing neuron distribution...")
    analysis_results = analyzer.analyze_distribution(neuron_data)
    print("Analysis results:")
    print(analysis_results)
    
    # Create visualizations
    print("\nCreating visualization...")
    plot_path = os.path.join(args.output_dir, 'neuron_distribution.png')
    plotter.plot_distribution(analysis_results, plot_path)
    
    print(f"\nAnalysis complete. Results saved to {args.output_dir}")

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
if __name__ == "__main__":
    main()