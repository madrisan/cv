#!/usr/bin/python

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

from experiences import jobs

def mnorm(month):
    """Normalize the month number."""
    return (month - 1) / 12.0

def jcolor(index, upper):
    """Return the plotter color associated to a job."""
    return plt.cm.Paired(np.linspace(0, 1, upper))[index]

def jindex(job):
    """Return the index of a 'job' in the vector 'jobs'."""
    return jobs.index(job)

def jparser(history, bullet_factor=2.2):
    """Parse the jobs history and initialize date, shape, jobtype, and color
       variables."""

    year, months, shape, jobtype, colors = ([] for _ in xrange(5))
    for job in history:
        ystart = job['year_start'][0] + mnorm(job['year_start'][1])
        yend = job['year_end'][0] + mnorm(job['year_end'][1])
        delta = yend - ystart
        assert(delta >= 0)

        yhalf = ystart + delta / 2.0
        year.append(yhalf)

        job_months = 12.0 * delta + 1
        months.append(job_months)

        shape.append(bullet_factor * job_months ** 2)
        job_index = jindex(job['type'])
        jobtype.append(job_index)
        colors.append(jcolor(job_index, len(jobs)))

    return year, shape, jobtype, colors

def make_jobs_plot((year, shape, jobtype, colors)):
    """Create the jobs history plot and legend"""

    def textlabel(sp, x, y, text, rotation='horizontal'):
        """Add a floating text to a subplot sp"""
        sp.text(x, y, text, style='italic', color='gray', fontsize=10,
                rotation=rotation)

    fig = plt.figure(1)

    ax = fig.add_subplot(111)
    ax.scatter(x=year, y=jobtype, s=shape, c=colors, alpha=0.5)

    # Get the current date
    now = datetime.datetime.now()

    # Add axis labels
    ax.set_xlabel('Year')
    ax.set_ylabel('Job Typology')
    ax.set_title('Job History')
    ax.set_xlim([1995, now.year + 3])
    ax.set_ylim([-1, len(jobs) + 1])

    # Add grid - fixme: yticks[] has to be manually adjusted
    yticks = [8, 11, 12]
    ax.set_yticks(yticks)
    ax.set_yticklabels([''])
    ax.grid('on')

    # Add a vertical line to show the current date
    xnow = now.year + mnorm(now.month) 
    ax.axvline(x=xnow, ymin=0.02, ymax=0.98, linewidth=1, color='0.75')

    # Add some text labels to hopefully improve the plot readability
    # fixme: the y coordinate has to be set manually
    textlabel(ax, 1995.4,  3.7, 'Development')
    textlabel(ax, 1995.4,  8.6, 'Linux system')
    textlabel(ax, 1995.4, 11.2, 'Monitoring')
    textlabel(ax, 1995.4, 12.2, 'Networking')
    textlabel(ax, xnow+0.05, 0.5, "%s.%s" % (now.year, now.month), rotation=45)

    # Add a legend
    handles = [mpatches.Patch(color=jcolor(jindex(job), len(jobs)),
                              label=job, alpha=0.8) for job in jobs]
    lgd = ax.legend(reversed(handles), reversed(jobs),
                    loc='upper right', bbox_to_anchor=(1.55, 0.8),
                    prop={'size': 12})

    return fig, lgd


from experiences import history
fig, legend = make_jobs_plot(jparser(history))

# Save the plot on a png file
filename = '../images/experiences.png'
fig.savefig(filename, bbox_extra_artists=(legend,), bbox_inches='tight')
