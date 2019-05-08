import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import ganim


print('Successfully imported', ganim.name)

ganim.set_up_style()

# font dictionary
font = {
    'family': 'serif',
    'name': 'Computer Modern Roman',
    'style': 'normal',
    'color': 'white',
    'weight': 'normal',
    'size': 20
}

x = np.linspace(-2, 2, 1000)
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.spines['left'].set_position(('data', 0.0))
ax1.spines['bottom'].set_position(('data', 0.0))
l1, l2, l3 = plt.plot(x, x*x, x, x*x*x, x, x*x*x*x)
ax1.grid(which='major', ls='dotted', alpha=.5)

plt.xticks([-2.0, -1.0, 0, 1.0, 2.0], ['$-2,0$', r'$-1,0$', '', '$1,0$', '$2,0$'])
plt.yticks([-5, 5, 10, 15], ['$-5$', '$5$', '$10$', '$15$'])

plt.title(
    r'\begin{center}' +
    r'An example of \LaTeX\ text in the graph.\\ ' +
    r'Functions $f(x) = x^n$ for $n \in \{2, 3, 4\}$' +
    r'\end{center}',
    fontdict=font
)

fig1.subplots_adjust(top=.8, right=.5)

fig1.text(
    .55,
    .55,
    r'Plus some text at the right side!' +
    '\n' +
    r'$$\frac{1}{\sin^2(x)}$$',
    fontdict=font
)

fig1.text(
    .55,
    .15,
    r'And a table:' +
    '\n' +
    r'$$\begin{array}{|c|c|}' +
    r'\hline ' +
    r'\rule{0ex}{2.5ex} x & x^2 \\\hline ' +
    r'1 & 1\\' +
    r'2 & 4\\' +
    r'3 & 9 \\' +
    r'\hline \end{array}$$',
    fontdict=font
)

plt.savefig('test00.svg')
