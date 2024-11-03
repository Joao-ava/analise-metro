import tkinter as tk
import networkx as nx
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from app.matrix import Matrix, LinearAlgebra


lines = [
    "Avenida", # 1
    "Centro", # 2
    "Praça", # 3
    "Parque", # 4
    "Shopping", # 5
    "Terminal", # 6
]

def convert_coordinates_to_string(positions):
    return [
        [lines[item[0] - 1], lines[item[1] - 1]]
        for item in positions
    ]


def not_in(positions, excludes):
    items = []
    for position in positions:
        is_valid = True
        for exclude in excludes:
            if position[0] == exclude[0] and position[1] == exclude[1]:
                is_valid = False
        
        if is_valid:
            items.append(position)

    return items


def make_graph(ax, matriz, show_reflective, show_symmetry, show_asymmetric, show_antisymmetric, show_transitive):
    graph = nx.DiGraph()
    positions = [
        [i, j]
        for i in range(1, matriz.rows + 1)
        for j in range(1, matriz.cols + 1)
    ]
    valid_positions = convert_coordinates_to_string(
        filter(
            lambda item: matriz.get(item[0], item[1]) != 0,
            positions
        )
    )
    graph.add_edges_from(convert_coordinates_to_string(positions))
    pos = nx.spring_layout(graph)

    arrow_size = 20
    nx.draw_networkx_nodes(graph, pos, node_color="#9977BB", node_size = 600, ax=ax)
    nx.draw_networkx_labels(graph, pos, ax=ax)

    other_edges = list(filter(lambda item: item[0] != item[1], valid_positions))
    diagonal_edges = list(filter(lambda item: item[0] == item[1], valid_positions))

    nx.draw_networkx_edges(graph, pos, edgelist=other_edges, edge_color='#44AAAA', arrows=True, arrowsize=arrow_size, ax=ax)
    nx.draw_networkx_edges(graph, pos, edgelist=diagonal_edges, edge_color='#552288', arrows=True, arrowsize=arrow_size, ax=ax)

    missing_edges_color = "#ff6347"
    not_symmetry_color = "#DDAA77"
    if show_reflective:
        edges = not_in(convert_coordinates_to_string(matriz.reflective_closure), valid_positions)
        nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color=missing_edges_color, arrows=True, arrowsize=arrow_size, ax=ax)

    if show_symmetry:
        edges = not_in(convert_coordinates_to_string(matriz.symetry_closure), valid_positions)
        nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color=missing_edges_color, arrows=True, arrowsize=arrow_size, ax=ax)

    if show_asymmetric:
        edges = convert_coordinates_to_string(matriz.asymmetric_closure)
        nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color=not_symmetry_color, arrows=True, arrowsize=arrow_size, ax=ax)

    if show_antisymmetric:
        edges = convert_coordinates_to_string(matriz.antisymmetric_closure)
        nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color=not_symmetry_color, arrows=True, arrowsize=arrow_size, ax=ax)

    if show_transitive:
        edges = not_in(convert_coordinates_to_string(matriz.transitive_closure), valid_positions)
        nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color=missing_edges_color, arrows=True, arrowsize=arrow_size, ax=ax)


def create_header(
    root,
    title,
    matriz: Matrix
):
    # Criação do frame para a interface
    frame_header = ttk.Frame(root, padding="10")

    # Adição do título
    title = ttk.Label(frame_header, text=title, font=("Helvetica", 16))
    title.grid(row=0, column=0, pady=(0, 10))

    # propriedades
    reflective_label = ttk.Label(
        frame_header,
        text="✅ É reflexiva" if matriz.reflective else "❌ Não é reflexiva",
        anchor="w",
        width=20
    )
    reflective_label.grid(row=1, column=0)

    symmetry_label = ttk.Label(
        frame_header,
        text="✅ É simetrica" if matriz.symmetry else "❌ Não é simetrica",
        anchor="w",
        width=20
    )
    symmetry_label.grid(row=1, column=1)

    asymmetric_label = ttk.Label(
        frame_header,
        text="✅ É assimétrica" if matriz.asymmetric else "❌ Não é assimétrica",
        anchor="w",
        width=20
    )
    asymmetric_label.grid(row=1, column=2)

    antisymmetric_label = ttk.Label(
        frame_header,
        text="✅ É anti-simetrica" if matriz.antisymmetric else "❌ Não é anti-simetrica",
        anchor="w",
        width=20
    )
    antisymmetric_label.grid(row=2, column=0)

    transitive_label = ttk.Label(
        frame_header,
        text="✅ É transitiva" if matriz.transitive else "❌ Não é transitiva",
        anchor="w",
        width=20
    )
    transitive_label.grid(row=2, column=1)

    equals_label = ttk.Label(
        frame_header,
        text="✅ É de equivalência" if matriz.equivalence else "❌ Não é equivalente",
        anchor="w",
        width=20
    )
    equals_label.grid(row=2, column=2)

    order_label = ttk.Label(
        frame_header,
        text="✅ É de " + matriz.order if matriz.order else "❌ Não é de ordem",
        anchor="w",
        width=20
    )
    order_label.grid(row=3, column=0)

    maximal_text = ttk.Label(
        frame_header,
        text="✅ Maximais: " + ", ".join([lines[item - 1] for item in matriz.maximal_elements]) if matriz.maximal_elements else "❌ Não a maximais",
        anchor="w",
        width=20
    )
    maximal_text.grid(row=3, column=1)

    minimal_text = ttk.Label(
        frame_header,
        text="✅ Minimais: " + ", ".join([lines[item - 1] for item in matriz.minimal_elements]) if matriz.minimal_elements else "❌ Não a minimais",
        anchor="w",
        width=20
    )
    minimal_text.grid(row=3, column=2)

    max_text = ttk.Label(
        frame_header,
        text="✅ Maior: " + ", ".join([lines[item - 1] for item in matriz.max]) if matriz.max else "❌ Não a maior",
        anchor="w",
        width=20
    )
    max_text.grid(row=4, column=0)

    min_text = ttk.Label(
        frame_header,
        text="✅ Menor: " + ", ".join([lines[item - 1] for item in matriz.min]) if matriz.min else "❌ Não a menor",
        anchor="w",
        width=20
    )
    min_text.grid(row=4, column=1)

    return frame_header


def create_filters_frame(
    root,
    matriz: Matrix,
    on_submit
):
    frame_bottom = ttk.Frame(root, padding="10")

    show_reflective = tk.BooleanVar(root, False)
    show_symmetry = tk.BooleanVar(root, False)
    show_asymmetric = tk.BooleanVar(root, False)
    show_antisymmetric = tk.BooleanVar(root, False)
    show_transitive = tk.BooleanVar(root, False)

    row = 0
    chk1 = ttk.Checkbutton(frame_bottom, text="Fecho reflexiva", variable=show_reflective)
    if not matriz.reflective:
        chk1.grid(row=row, column=0)
        row += 1

    chk2 = ttk.Checkbutton(frame_bottom, text="Fecho simetria", variable=show_symmetry)
    if not matriz.symmetry:
        chk2.grid(row=row, column=0)
        row += 1

    chk3 = ttk.Checkbutton(frame_bottom, text="Fecho assimetria", variable=show_asymmetric)
    if not matriz.asymmetric:
        chk3.grid(row=row, column=0)
        row += 1

    chk4 = ttk.Checkbutton(frame_bottom, text="Fecho anti-simetria", variable=show_antisymmetric)
    if not matriz.antisymmetric:
        chk4.grid(row=row, column=0)
        row += 1

    chk5 = ttk.Checkbutton(frame_bottom, text="Fecho transitiva", variable=show_transitive)
    if not matriz.transitive:
        chk5.grid(row=row, column=0)
        row += 1

    def command():
        on_submit(
            show_reflective.get(),
            show_symmetry.get(),
            show_asymmetric.get(),
            show_antisymmetric.get(),
            show_transitive.get()
        )

    btn = ttk.Button(frame_bottom, text="Gerar", command=command)
    btn.grid(row=row, column=0)
    return frame_bottom


def make_screen(root, title, matriz):
    frame = ttk.Frame(root)

    frame_header = create_header(
        frame,
        title,
        matriz
    )
    frame_header.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    fig = Figure(figsize=(7, 5), dpi=100)
    ax = fig.add_subplot(111)# Adiciona o gráfico ao Tkinter

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().grid(row=1, column=0, pady=10)

    def update_graph(show_reflective=False, show_symmetry=False, show_asymmetric=False, show_antisymmetric=False, show_transitive=False):
        ax.clear()

        canvas.get_tk_widget().grid(row=1, column=0, pady=10)
        make_graph(ax, matriz, show_reflective, show_symmetry, show_asymmetric, show_antisymmetric, show_transitive)
        canvas.draw()


    update_graph()

    frame_bottom = create_filters_frame(frame, matriz, update_graph)
    frame_bottom.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # frame.pack(fill='both', expand=True)
    frame.grid(row=0, column=0)
    return frame

# Função principal do app
def main():
    # Criação da janela principal
    root = tk.Tk()
    root.title("Análise de Metrô")

    notebook = ttk.Notebook(root)

    metro = Matrix(6, 6, [ 
        1, 1, 0, 0, 0, 0,
        1, 1, 1, 0, 0, 1,
        0, 0, 1, 0, 0, 0,
        0, 0, 0, 1, 0, 1,
        0, 0, 0, 1, 1, 1,
        0, 1, 0, 0, 1, 1
    ])
    notebook.add(make_screen(notebook, "Análise de Metrô", metro), text="Análise de Metrô")

    bus = Matrix(6, 6, [
        0, 1, 0, 0, 0, 1,
        1, 0, 0, 1, 0, 0,
        0, 0, 0, 1, 0, 0,
        0, 1, 1, 0, 0, 1,
        0, 0, 0, 0, 0, 1,
        1, 0, 0, 1, 1, 0
    ])
    notebook.add(make_screen(notebook, "Análise de Ônibus", bus), text="Análise de Ônibus")

    composition = LinearAlgebra.dot(metro, bus)
    notebook.add(make_screen(notebook, "Análise de Composição Metrô e Ônibus", composition), text="Análise de Composição Metrô e Ônibus")

    notebook.grid(row=0, column=0)

    # Início do loop principal do Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
