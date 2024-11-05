from graph_data import graph_data
import permutation

graph = graph_data[0]


if __name__ == "__main__":
    all_permutations = permutation.generate_permutations(len(graph))
    all_cycles = permutation.find_cycles(graph)
    optimal_cycles = permutation.find_best_cycle(graph)
    print("All permutations: ")
    print(all_permutations)
    print("All Hamiltonian cycles: ")
    print(all_cycles)
    print("Optimal Cycle:")
    if optimal_cycles != -1:
        best_distance = permutation.cycle_distance(optimal_cycles, graph)
        print(f"Cycle: {optimal_cycles}  Distance: {best_distance}")
    else:
        print("No valid Hamiltonian cycle found.")
