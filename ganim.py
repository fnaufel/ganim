import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

name = 'ganim'


def set_up_style():
    """
    Define estilos do matplotlib a ser usados.
    """

    # TODO: LaTeX: linhas de array e de fração estão finas demais.

    # TODO:
    #   figure.dpi não tem efeito no arquivo .svg?
    #   Abrir no ImageMagick?

    # TODO: Adicionar setas aos eixos (spines).

    # TODO: Completar parâmetros abaixo.

    my_style = {
        'axes.edgecolor': 'y',
        'axes.facecolor': 'k',
        'axes.formatter.use_mathtext': True,
        'axes.labelcolor': 'w',
        'axes.linewidth': 1.0,
        'axes.spines.right': False,
        'axes.spines.top': False,
        'axes.spines.left': True,
        'axes.spines.bottom': True,
        'figure.dpi': 200,
        'figure.edgecolor': 'k',
        'figure.facecolor': 'k',
        'figure.figsize': [12.8, 7.15],
        'font.family': ['serif'],
        'font.serif': ['Computer Modern Roman'],
        'patch.edgecolor': 'white',
        'savefig.dpi': 200,
        'savefig.edgecolor': 'k',
        'savefig.facecolor': 'k',
        'text.color': 'w',
        'text.latex.preamble': [
            r'\usepackage{xcolor}',
            r'\usepackage{euler}',
            r'\usepackage{amsmath}',
        ],
        'text.usetex': True,
        'xtick.color': 'y',
        'xtick.direction': 'inout',
        'ytick.color': 'y',
        'ytick.direction': 'inout',
    }

    matplotlib.style.use(my_style)


def create_scene(with_axes=False):
    """
    Criar uma nova cena.

    :param with_axes: se True, desenhar os eixos.

    :return:
      (fig, ax): instância de Figure e instância de Axes.
    """
    fig, ax = plt.subplots()
    if not with_axes:
        ax.set_axis_off()

    return fig, ax


def animate_segment(ax, point_a, point_b, n_frames=100, effect='grow', color='w', linewidth=1):
    """
    Gera os frames da animação de um segmento.

    :param ax: axes no qual desenhar.
    :param point_a: ponto inicial.
    :param point_b: ponto final.
    :param n_frames: quantidade de frames.
    :param effect: efeito a ser aplicado.

    :return:
      animate_segment_func: função a ser chamada por `FuncAnimation`.
    """

    # TODO: adicionar opção de velocidade de animação: slow, medium, fast (dicionário com estas chaves).
    if effect == 'grow':
        xa, ya = point_a
        xb, yb = point_b
        dx = (xb - xa) / n_frames
        dy = (yb - ya) / n_frames

        def animate_segment_func(i):
            # TODO: esta função usa escopo léxico.
            #   Manter assim ou usar fargs de FuncAnimation?
            """
            Função a ser chamada por `FuncAnimation` para desenhar um frame da animação do segmento.

            :param i: número do frame a ser desenhado.
            """

            # Calcular incrementos dx e dy de cada frame
            x = xa + i * dx
            y = ya + i * dy
            # Desenhar segmento
            ax.plot((xa, x), (ya, y), scalex=False, scaley=False, linewidth=linewidth, color=color)
    else:
        raise ValueError(f'Unknown effect: {effect}')

    return animate_segment_func


def render_scene(fig, func, frames=100, interval=25):
    """
    Renderiza a cena.

    :param fig: figura.
    :param func: função a ser chamada por `FuncAnimation`.
    :param frames: total de frames.
    :param interval: intervalo entre trocas de frames (em ms).

    :return: instância de `FuncAnimation`.
    """

    # TODO: fazer com que esta função receba uma lista de funções para desenhar.
    #   Definir aqui uma função interna que percorre a lista de funções, executando-as.
    #   Passar esta função interna para FuncAnimation.

    scene = FuncAnimation(
            fig,
            func,
            frames=frames,
            interval=interval
    )

    return scene
