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

    expr_types, expr_map = experiences
    years, areas, experiences, colors = ([] for _ in range(4))

    for e in expr_map:
        years.append(e.date)
        areas.append(np.pi * (area_adj * e.period)**2)
        experiences.append(e.type)
        colors.append(e.color)

    fig = plt.figure(1)

    ax = fig.add_subplot(111)
    ax.scatter(x=years, y=experiences, s=areas, c=colors, alpha=0.5)

    # Get the current date
    now = datetime.datetime.now()

    # Add axis labels
    ax.set_xlabel('Year')
    ax.set_ylabel('Experiences')
    ax.set_title('Job and Lifelong Learning History')
    ax.set_xlim([1995, now.year + 3])
    ax.set_ylim([-1, len(expr_types) + 1])

    # Add grid - fixme: yticks[] if set must to be manually adjusted
    yticks = []
    ax.set_yticks(yticks)
    ax.set_yticklabels([''])
    ax.grid('off')

    vlinestyle = 'dashdot'

    # Start of Job
    ax.axvline(x=1999.6, ymin=0.02, ymax=0.98,
               linewidth=1, linestyle=vlinestyle, color='0.75')

    # Mark the move to France
    ax.axvline(x=2008.6, ymin=0.02, ymax=0.98,
               linewidth=1, linestyle=vlinestyle, color='0.75')
    textlabel(ax, 2007.9, -0.7, 'it')
    textlabel(ax, 2008.9, -0.7, 'fr')

    # Mark the start of the OS2 Micro-Entrepreneur activity
    ax.axvline(x=2013.4, ymin=0.02, ymax=0.98,
               linewidth=1, linestyle=vlinestyle, color='0.75')
    textlabel(ax, 2013.5, 14.4, 'OS2')

    # Mark the start of the amazing MOOCs experience
    ax.axvline(x=2014.10, ymin=0.02, ymax=0.98,
               linewidth=1, linestyle=vlinestyle, color='0.75')
    textlabel(ax, 2014.3, 13.9, 'MOOCs')

    # Add a vertical line to show the current date
    xnow = now.year + normalize(now.month)
    ax.axvline(x=xnow, ymin=0.02, ymax=0.98,
               linewidth=1, linestyle=vlinestyle, color='0.75')
    textlabel(ax, xnow + 0.05, 0.2,
              "{0}.{1}".format(now.year, now.month), rotation=45)

    # Add some text labels to hopefully improve the plot readability
    # fixme: the y coordinates must to be manually set
    textlabel(ax, 1995.4,   3.2, 'Maths')
    textlabel(ax, 1995.4,   2.6, 'Cryptography, AI')
    textlabel(ax, 1995.4,   2.0, 'C/C++/MatLab Programming')
    textlabel(ax, 1997.0,   6.8, 'TeX')
    textlabel(ax, 1997.0,   6.2, 'Development')
   #textlabel(ax, 1998.6,  -0.6, 'C/C++/Java Programming')

    textlabel(ax, 2000.3,   9.6, 'Cisco WAN')
    textlabel(ax, 2000.3,   9.0, 'Networking')
   #textlabel(ax, 2000.3,   8.4, '@FIAT/IBM, BT')

    textlabel(ax, 2003.0,  12.4, 'Nagios')
    textlabel(ax, 2005.0,   2.0, 'Linux system Development')
    textlabel(ax, 2006.0,   1.4, 'QiLinux / openmamba')
    textlabel(ax, 2006.4,   5.2, 'Shell scripting')

    textlabel(ax, 2007.2,   9.9, 'Linux SysAdmin')
   #textlabel(ax, 2007.2,   9.3, '@IBM')

    textlabel(ax, 2011.10, 13.3, 'System and Applications')
    textlabel(ax, 2011.10, 12.7, 'Monitoring')
   #textlabel(ax, 2011.10, 12.1, '@IBM')

    textlabel(ax, 2014.8,  11.3, 'DevOps')
    textlabel(ax, 2015.0,  10.7, 'IaC')
   #textlabel(ax, 2015.0,  10.1, '@Sopra-Steria')

   #textlabel(ax, 2013.0,  8.4,  'Angular')
   #textlabel(ax, 2013.0,  7.8,  'Node.js')
    textlabel(ax, 2013.9,  7.1,  'MEAN Stack')
    textlabel(ax, 2006.0,  7.2,  'PHP')
   #textlabel(ax, 2013.0,  6.6,  'Web Full Stack')
    textlabel(ax, 2013.1,  4.4,  'Python')
    textlabel(ax, 2014.4,  0.0,  'C')
    textlabel(ax, 2014.12, 1.4,  'BigData/ML')
    textlabel(ax, 2015.11, 2.2,  'Scala')
    textlabel(ax, 2015.3, -0.6,  'CUDA')
    textlabel(ax, 2016.0,  3.5,  'Math')
    textlabel(ax, 2016.2,  4.3,  'SaltStack')

    # Add a legend
    handles = \
        list(mpatches.Patch(color=getcolor(expr_types.index(e), len(expr_types)),
             label=e, alpha=0.8) for e in expr_types)
    lgd = ax.legend(reversed(handles), reversed(expr_types),
                    loc='upper right', bbox_to_anchor=(1.55, 0.8),
                    prop={'size': 10})

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
