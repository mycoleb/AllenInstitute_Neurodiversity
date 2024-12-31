# scripts/analyze_neuron_types.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data.data_loader import BrainDataLoader
from src.analysis.neuron_types import NeuronAnalyzer
from src.visualization.plotters import NeuronPlotter
import argparse

def main():
    parser = argparse.ArgumentParser(description='Analyze neuron types in brain regions')
    parser.add_argument('--region-id', type=int, help='ID of brain region to analyze')
    parser.add_argument('--output-dir', type=str, default='output', help='Directory for output files')
    args = parser.parse_args()

    # Initialize components
    loader = BrainDataLoader()
    analyzer = NeuronAnalyzer()
    plotter = NeuronPlotter()

    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    # Get data
    if args.region_id:
        print(f"Analyzing region ID: {args.region_id}")
        neuron_data = loader.get_neuron_data(args.region_id)
    else:
        print("Analyzing all regions")
        neuron_data = loader.get_neuron_data()

    # Analyze data
    analysis_results = analyzer.analyze_distribution(neuron_data)
    
    # Create visualizations
    plot_path = os.path.join(args.output_dir, 'neuron_distribution.png')
    plotter.plot_distribution(analysis_results, plot_path)
    
    print(f"Analysis complete. Results saved to {args.output_dir}")

if __name__ == "__main__":
    main()