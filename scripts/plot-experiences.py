#!/usr/bin/python3

# Create a scatter plot for visualizing all my job experences and
# programming activities.
#
# Copyright (C) 2016 Davide Madrisan <davide.madrisan.gmail.com>

import matplotlib
matplotlib.use('Agg')
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

import datetime
import numpy as np

def normalize(month):
    """Normalize the month number."""
    assert(month in range(13))
    return (month - 1) / 12.0

def getcolor(index, upper):
    """Return the plotter color associated to an experience."""
    assert(index in range(upper))
    return plt.cm.Paired(np.linspace(0, 1, upper))[index]

def parser(source):
    """Parse the history file and returns a list containing the
       experiences type and map of all the experiences."""

    skip_line = lambda line: line.startswith('#') or not line.strip()
    date = lambda sy, sm, ey, em: \
        (int(ey) + normalize(int(em)) + int(sy) + normalize(int(sm))) / 2.0
    months = lambda sy, sm, ey, em: \
        12*(int(ey) - int(sy)) + int(em) - int(sm)

    def row_iter(file_obj):
        return (nextline.strip().split(',')
            for nextline in file_obj if not skip_line(nextline))

    def my_experiences(experience_iter):
        return tuple((
            date(sy, sm, ey, em), months(sy, sm, ey, em), e.strip())
            for sy, sm, ey, em, e in experience_iter)

    with open(source, "r") as data:
        history = my_experiences(row_iter(data))
        expr_types = sorted(set([expr[2] for expr in history]))

        index = lambda e: expr_types.index(e)
        color = lambda e: getcolor(index(e), len(expr_types))
        expr_map = map(lambda e:
            (e[0], e[1], index(e[2]), color(e[2])), history)

    return expr_types, expr_map

def make_jobs_plot(experiences, area_adj=0.84):
    """Create the jobs history plot and legend"""

    def textlabel(sp, x, y, text, rotation='horizontal'):
        """Add a floating text to a subplot 'sp'"""
        sp.text(x, y, text, style='italic', color='gray', fontsize=10,
                rotation=rotation)

    expr_types, expr_map = experiences
    years, area, experiences, colors = ([] for _ in range(4))

    for e in expr_map:
        years.append(e[0])
        area.append(np.pi * (area_adj * e[1])**2)
        experiences.append(e[2])
        colors.append(e[3])

    fig = plt.figure(1)

    ax = fig.add_subplot(111)
    ax.scatter(x=years, y=experiences, s=area, c=colors, alpha=0.5)

    # Get the current date
    now = datetime.datetime.now()

    # Add axis labels
    ax.set_xlabel('Year')
    ax.set_ylabel('Experiences')
    ax.set_title('Job History')
    ax.set_xlim([1995, now.year + 3])
    ax.set_ylim([-1, len(expr_types) + 1])

    # Add grid - fixme: yticks[] has to be manually adjusted
    yticks = []
    ax.set_yticks(yticks)
    ax.set_yticklabels([''])
    ax.grid('on')

    # Add a vertical line to show the current date
    xnow = now.year + normalize(now.month)
    ax.axvline(x=xnow, ymin=0.02, ymax=0.98, linewidth=1, color='0.75')

    # Add some text labels to hopefully improve the plot readability
    # fixme: the y coordinate has to be set manually
    textlabel(ax, 1995.4,  2.6, 'Development')
    textlabel(ax, 1995.4,  9.0, 'Networking')
    textlabel(ax, 1995.4, 11.2, 'Linux system')
    textlabel(ax, 1995.4, 13.0, 'Monitoring')
    textlabel(ax, xnow+0.05, 0.5, "%s.%s" % (now.year, now.month), rotation=45)

    # Add a legend
    handles = \
        list(mpatches.Patch(color=getcolor(expr_types.index(e), len(expr_types)),
             label=e, alpha=0.8) for e in expr_types)
    lgd = ax.legend(reversed(handles), reversed(expr_types),
                    loc='upper right', bbox_to_anchor=(1.55, 0.8),
                    prop={'size': 10})

    return fig, lgd

def main():
    source = 'experiences.csv'
    picture = '../images/experiences.png'

    fig, legend = make_jobs_plot(parser(source))
    fig.savefig(picture, bbox_extra_artists=(legend,), bbox_inches='tight')
    print('The picture has been saved as', picture)

if __name__ == '__main__':
    main()
