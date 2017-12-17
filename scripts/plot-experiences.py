#!/usr/bin/python3

# Create a scatter plot for visualizing all my job experences and
# programming activities.
# Note that Python 3 is required.
#
# Copyright (C) 2016-2017 Davide Madrisan <davide.madrisan.gmail.com>

import matplotlib
matplotlib.use('Agg')
matplotlib.rc('font', family='sans-serif')
matplotlib.rc('text', usetex=True)
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from collections import namedtuple
import datetime
import numpy as np
import getopt
import sys

Experience = namedtuple('Experience', ['date', 'period', 'type', 'color'])

def die(message):
    sys.exit('{}: {}'.format(__file__, message))

def getcolor(index, upper):
    """Return a progressive color for an index in range(upper)."""
    assert(index in range(upper))
    return plt.cm.Paired(np.linspace(0, 1, upper))[index]

def normalize(month):
    """Normalize the month number."""
    assert(month in range(13))
    return (month - 1) / 12.0

def parser(source):
    """Parse the history file and returns a list containing the
       experience labels and a map of all the Experience's."""

    skip_line = lambda line: line.startswith('#') or not line.strip()
    date = lambda sy, sm, ey, em: \
        (int(ey) + normalize(int(em)) + int(sy) + normalize(int(sm))) / 2.0
    months = lambda sy, sm, ey, em: \
        12 * (int(ey) - int(sy)) + int(em) - int(sm)

    def row_iter(file_obj):
        return (nextline.strip().split(',')
            for nextline in file_obj if not skip_line(nextline))

    def my_experiences(experience_iter):
        return tuple((date(*date_start_end), months(*date_start_end), e.strip())
            for *date_start_end, e in experience_iter)

    try:
        with open(source, "r") as data:
            history = my_experiences(row_iter(data))
            expr_types = sorted(set([expr[2] for expr in history]))

            index = lambda e: expr_types.index(e)
            color = lambda e: getcolor(index(e), len(expr_types))
            expr_map = map(lambda e:
                Experience(e[0], e[1], index(e[2]), color(e[2])), history)
    except FileNotFoundError as err:
        die(err)

    return expr_types, expr_map

def make_jobs_plot(experiences, area_adj=0.84):
    """Create the jobs history plot and legend"""

    def textlabel(sp, x, y, text, rotation='horizontal'):
        """Add a floating text to a subplot 'sp'"""
        sp.text(x, y, text, style='italic', color='gray', fontsize=10,
                rotation=rotation)

    # Get the current date
    now = datetime.datetime.now()

    # Consolidate the data about job experiences
    expr_types, expr_map = experiences
    years, areas, experiences, colors = ([] for _ in range(4))
    for e in expr_map:
        years.append(e.date)
        areas.append(np.pi * (area_adj * e.period)**2)
        experiences.append(e.type)
        colors.append(e.color)

    fig, ax = plt.subplots()

    # Create a scatter plot with the job experiences
    ax.scatter(x=years, y=experiences, s=areas, c=colors, alpha=0.5)

    # Add axis labels
    xmin, xmax = 1995, now.year + 3
    ax.set_xlabel('Year')
    ax.set_ylabel('Experiences')
    ax.set_title('Job and Lifelong Learning History')
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([-1, len(expr_types) + 1])

    # Add grid - fixme: yticks[] if set must to be manually adjusted
    yticks = []
    ax.set_yticks(yticks)
    ax.set_yticklabels([''])
    ax.grid('off')

    # Add vertical dotted lines at the major steps of my working life
    xnow = now.year + normalize(now.month)
    ytop = 14.5
    vdotlines = [
        (1999.6, 'work.IT', ytop, 'horizontal'),  # Start of the working life
        (2008.6, 'work.FR', ytop, 'horizontal'),  # Move to South of France
        # OS2 Micro-Entrepreneur activity
        (2013.4, 'OS2', ytop, 'horizontal'),
        # Start of the amazing MOOCs experience :)
        (2014.10, 'MOOCs', ytop-.5, 'horizontal'),
        (xnow, '{0}.{1}'.format(now.year, now.month), .2, 45)]
    ymin, ymax, linewidth, linecolor = 0.02, 0.98, 1, '0.75'

    for (x, label, ylabel, label_rotation) in vdotlines:
        ax.axvline(x=x, ymin=ymin, ymax=ymax,
                   linewidth=linewidth, linestyle='dashdot', color=linecolor)
        textlabel(ax, x+.1, ylabel, label, rotation=label_rotation)

    # Add some text labels to hopefully improve the plot readability
    # fixme: the y coordinates must to be manually set
    annotations = [
        (1995.4,   3.2, 'Maths'),
        (1995.4,   2.6, 'Cryptography, AI'),
        (1995.4,   2.0, 'C/C++/MatLab Programming'),
        (1997.0,   6.8, 'TeX'),
        (1997.0,   6.2, 'Development'),
       #(1998.6,  -0.6, 'C/C++/Java Programming'),
        (2000.3,   9.6, 'Cisco WAN'),
        (2000.3,   9.0, 'Networking'),
       #(2000.3,   8.4, '@FIAT/IBM, BT'),
        (2003.0,  12.4, 'Nagios'),
        (2005.0,   2.0, 'Linux system Development'),
        (2006.0,   1.4, 'QiLinux / openmamba'),
        (2006.4,   5.2, 'Shell scripting'),
        (2007.2,   9.9, 'Linux SysAdmin'),
       #(2007.2,   9.3, '@IBM'),
        (2011.10, 13.3, 'System and Applications'),
        (2011.10, 12.7, 'Monitoring'),
       #(2011.10, 12.1, '@IBM'),
        (2015.0,  11.1, 'DevOps'),
        (2015.6,  10.5, 'IaC'),
       #(2015.0,  10.1, '@Sopra-Steria'),
       #(2013.0,  8.4,  'Angular'),
       #(2013.0,  7.8,  'Node.js'),
        (2013.9,  7.1,  'MEAN Stack'),
        (2006.0,  7.2,  'PHP'),
       #(2013.0,  6.6,  'Web Full Stack'),
        (2013.1,  4.4,  'Python'),
        (2014.4,  0.0,  'C'),
        (2014.12, 1.4,  'BigData/ML'),
        (2015.11, 2.2,  'Scala'),
        (2015.3, -0.6,  'CUDA'),
        (2016.0,  3.5,  'Math'),
        (2016.2,  4.3,  'SaltStack')]
    for x, y, label in annotations:
        textlabel(ax, x, y, label)

    # Add a legend
    handles = \
        list(mpatches.Patch(color=getcolor(expr_types.index(e), len(expr_types)),
             label=e, alpha=0.8) for e in expr_types)
    lgd = ax.legend(reversed(handles), reversed(expr_types),
                    loc='upper right', bbox_to_anchor=(1.55, 0.8),
                    prop={'size': 10})

    ax2 = ax.twinx()
    years = np.arange(2000-.35, now.year+.35, 1)
    courses = [
        1, 1, 1, 2, 0, 0, 0, 1,
        # 2008: Moving to France... 'formation continue' :P
        0, 0, 0, 0, 0, 0,
        # 2014: MOOCs start here, for me at least
        3, 23, 20, 9]
    ax2.bar(years, courses, width=.7, color='lightblue', alpha=0.1)
    fig.tight_layout()

    return fig, lgd

def usage():
    progname = sys.argv[0]
    print('Usage: {0} csv=<input-file> image=<out-file>'.format(progname))

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'c:i:h',
            ["csv=", "image=", "help"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit()
        elif o in ('-c', '--csv'):
            source = a
        elif o in ('-i', '--image'):
            image = a

    fig, legend = make_jobs_plot(parser(source))
    try:
        fig.savefig(image, bbox_extra_artists=(legend,), bbox_inches='tight')
        print('The image has been saved as', image)
    except OSError as err:
        die('Cannot create the plot: {}'.format(err))

if __name__ == '__main__':
    main()
