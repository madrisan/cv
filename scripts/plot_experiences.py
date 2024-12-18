#!/usr/bin/python3

"""
Create a scatter plot for visualizing all my job experences and
programming activities. Python 3 is required.

Copyright (C) 2016-2024 Davide Madrisan <d.madrisan.proton.me>
"""

from collections import namedtuple
import datetime
import sys
from typing import Dict, List, Tuple

import click
import numpy as np
import scipy.interpolate

import matplotlib

matplotlib.use("Agg")
matplotlib.rc("font", family="sans-serif")
matplotlib.rc("text", usetex=True)

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

Experience = namedtuple("Experience", ["date", "period", "type", "color"])


def die(message: str):
    """
    Print an error message and abort the script.

    Args:
        message (str): The error message.
    """
    sys.exit(f"{__file__}: {message}")


def getcolor(index: int, upper: int):
    """
    Return a progressive color for an index in range(upper).
    """
    assert index in range(upper)
    return plt.cm.Spectral(np.linspace(1, 0, upper, endpoint=False))[index]


def normalize(month: int) -> float:
    """
    Normalize the month number.
    """
    assert month in range(13)
    return (month - 1) / 12.0


def parser(csv: str) -> Tuple[List[int], Dict[str, str]]:
    """
    Parse the history file and returns a list containing the
    experience labels and a map of all the Experience's.
    """
    skip_line = lambda line: line.startswith("#") or not line.strip()
    date = (
        lambda sy, sm, ey, em: (
            int(ey) + normalize(int(em)) + int(sy) + normalize(int(sm))
        )
        / 2.0
    )
    months = lambda sy, sm, ey, em: 12 * (int(ey) - int(sy)) + int(em) - int(sm)

    def row_iter(file_obj):
        return (
            nextline.strip().split(",")
            for nextline in file_obj
            if not skip_line(nextline)
        )

    def my_experiences(experience_iter):
        return tuple(
            (date(*date_start_end), months(*date_start_end), e.strip())
            for *date_start_end, e in experience_iter
        )

    try:
        with open(csv, "r", encoding="utf-8") as data:
            history = my_experiences(row_iter(data))
            expr_types = sorted({expr[2] for expr in history})
            index = lambda e: expr_types.index(e)
            color = lambda e: getcolor(index(e), len(expr_types))
            expr_map = map(
                lambda e: Experience(e[0], e[1], index(e[2]), color(e[2])), history
            )
    except FileNotFoundError as err:
        die(err)

    return expr_types, expr_map


def make_jobs_plot(experiences, area_adj):
    """Create the jobs history plot and legend"""

    def textlabel(sp, x, y, text, rotation="horizontal"):
        """Add a floating text to a subplot 'sp'"""
        sp.text(
            x, y, text, style="italic", color="dimgray", fontsize=9, rotation=rotation
        )

    # A text color suitable for both light and dark modes
    text_color = "green"  # "#FF4500"

    # Get the current date
    now = datetime.datetime.now()

    # Consolidate the data about job experiences
    expr_types, expr_map = experiences
    years, areas, experiences, colors = ([] for _ in range(4))
    for e in expr_map:
        years.append(e.date)
        areas.append(np.pi * (area_adj * e.period) ** 2)
        experiences.append(e.type)
        colors.append(e.color)
    assert len(years) == len(experiences)

    # Change the color of the image frame
    matplotlib.rc("axes", edgecolor="lightgray")

    fig, ax = plt.subplots()

    # Create a scatter plot with the job experiences
    ax.scatter(x=years, y=experiences, s=areas, c=colors, alpha=0.65)

    # Add axis labels
    xmin, xmax = 1995, now.year + 2
    # ax.set_xlabel('Year')
    # ax.set_ylabel('Experiences')
    # ax.set_title('Job and Lifelong Learning History')
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([-1, len(expr_types) + 1])

    # Add grid - fixme: yticks[] if set must to be manually adjusted
    ax.set_yticks([])
    ax.tick_params(labelcolor=text_color, length=0)

    # Add vertical dotted lines at the major steps of my working life
    xnow = now.year + normalize(now.month)
    ytop = 16.4
    vdotlines = [
        (
            1999.6,
            "$\\rightarrow$ work@it",
            ytop,
            "horizontal",
        ),  # Start of the working life
        (
            2008.6,
            "$\\rightarrow$ work@fr",
            ytop,
            "horizontal",
        ),  # Move to South of France
        # OS2 Micro-Entrepreneur activity
        (2013.4, "OS2", ytop, "horizontal"),
        # Start of the amazing MOOCs experience :)
        (2014.10, "MOOCs", ytop - 0.5, "horizontal"),
        (xnow, f"{now.year}.{now.month}", 0.6, 75),
    ]
    ymin, ymax, linewidth, linecolor = 0.02, 0.98, 0.8, "0.75"

    for x, label, ylabel, label_rotation in vdotlines:
        ax.axvline(
            x=x,
            ymin=ymin,
            ymax=ymax,
            linewidth=linewidth,
            linestyle="dotted",
            color=linecolor,
        )
        textlabel(ax, x + 0.1, ylabel, label, rotation=label_rotation)

    # Add some text labels to hopefully improve the plot readability
    # fixme: the y coordinates should not be manually set
    annotations = [
        (1995.7, 5.1, "Maths"),
        (1995.7, 4.5, "Cryptography, AI"),
        (1995.7, 3.9, "C/C++/MatLab"),
        (1997.0, 9.0, "T\\kern -.1667em\\lower .5ex\\hbox {E}\\kern -.125emX"),
        (1997.0, 8.4, "Development"),
        # (1998.6,  -0.6, 'C/C++/Java Programming'),
        (2000.3, 11.0, "Cisco WAN"),
        (2000.4, 10.4, "Networking"),
        # (2000.3,  10.4, '@FIAT/IBM, BT'),
        (2002.8, 14.1, "Nagios"),
        (2004.2, 3.8, "Linux system Development"),
        (2004.8, 3.2, "QiLinux / openmamba"),
        (2006.5, 7.2, "Shell scripting"),
        (2006.5, 10.9, "Linux SysAdmin"),
        # (2007.2,  10.3, '@IBM'),
        (2010.3, 15.3, "Nagios"),
        (2009.8, 14.7, "Centreon"),
        # (2011.10, 13.1, '@IBM'),
        (2014.9, 14.2, "DevOps"),
        (2018.0, 14.2, "Salt"),
        (2013.4, 12.9, "IaC"),
        # (2015.0,  10.1, '@Sopra-Steria'),
        # (2013.0,   8.4, 'Angular'),
        # (2013.0,   7.8, 'Node.js'),
        (2014.9, 8.9, "MEAN Stack"),
        (2006.0, 9.1, "PHP"),
        # (2013.0,   6.6, 'Web Full Stack'),
        (2013.8, 6.4, "Python"),
        (2016.1, 0.3, "C"),
        (2014.10, 1.4, "BigData/ML"),
        (2016.4, 3.4, "Scala"),
        (2016.0, -0.7, "CUDA"),
        (2016.7, 12.8, "Docker/Podman"),
        (2016.0, 5.4, "Math"),
        (2016.8, 15.5, "Xymon"),
        (2016.4, 11.3, "OpenStack"),
        (2019.8, 3.3, "Go"),
        (2019.2, 15.5, "Zabbix"),
        (2020.4, 11.8, "k8s"),
        (2020.6, 1.7, "GitLab CI"),
        (2020.8, 1.0, "ArgoCD"),
    ]
    for x, y, label in annotations:
        textlabel(ax, x, y, label)

    # Add a legend

    # prepend and extra entry for certifications, courses, and moocs
    # with a fixed color 'lightblue'
    expr_types = ["Certifications / Courses / MOOCs"] + expr_types
    legend_color = lambda i, size: getcolor(i, size) if i > 0 else "lightblue"

    handles = list(
        (
            mpatches.Patch(
                color=legend_color(expr_types.index(e), len(expr_types)),
                label=e,
                alpha=0.8,
            )
            for e in expr_types
        )
    )

    lgd = ax.legend(
        handles[::-1],
        expr_types[::-1],
        bbox_to_anchor=(1.55, 0.95),
        fontsize="small",
        prop={"size": 9},
        frameon=False,
    )
    for text in lgd.get_texts():
        text.set_color(text_color)

    # Add a bar plot for displaying courses/books and completed MOOCs
    ax2 = ax.twinx()
    bar_color = "lightblue"
    bar_width = 0.7
    years = np.arange(1995 - (bar_width / 2), now.year + (bar_width / 2), 1)
    courses = [
        10,
        10,
        10,
        4,
        # 1999: start of work life
        0,
        1,
        1,
        1,
        2,
        0,
        0,
        0,
        1,
        # 2008: Moving to France... 'formation continue' :P
        0,
        0,
        0,
        0,
        0,
        0,
        # 2014: MOOCs start here, for me at least
        #       web data programming db cloud compscience math sciences other health green-tech psychology
        # 2014        3
        3,
        # 2015   6    8      5        -   2       -         -    -        2
        23,
        # 2016  12    -      2        2   1       2         -    -        1
        20,
        # Now that MOOCs are most of the time paid courses, I started
        # by coupling them with [e-]books...
        # 2017   -    -      -        -   3       -         2    -        4
        9,
        # 2018   -    -      -        -   -       -         1    -        -
        2,
        # 2019   -    -      -        -   -       -         1    -        -
        1,
        # 2020   -    -      -        -   -       -         -    1        -    3
        4,
        # 2021   -    -      -        -   1       -         -    -        -    1       4          1
        7,
        # 2022   -    -      1        -   -       -         -    -        -    -       -          -
        1,
        # 2023
        0,
        # 2024
        0,
    ]
    ax2.bar(years, courses, width=bar_width, color=bar_color, alpha=0.2)
    ax2.set_yticks([])

    # Add a spline that interpolates the number of completed courses
    xnew = np.linspace(years.min(), years.max(), 100)
    fysmooth = scipy.interpolate.interp1d(years, courses, kind="quadratic")
    ysmooth = [fysmooth(ti) for ti in xnew]
    ax3 = ax2.twinx()
    ax3.set_frame_on(False)
    ax3.set_yticks([])
    ax3.plot(xnew, ysmooth, color=bar_color, alpha=0.4)

    return fig, lgd


@click.command()
@click.option(
    "--csv",
    help="Path of the CSV file containing the list of job experiences.",
    type=click.Path(exists=True, dir_okay=False),
)
@click.option(
    "--image",
    help="Path of the output PNG image.",
    type=click.Path(exists=True, dir_okay=False),
)
def main(csv, image):
    """Plots an IMAGE according to a CSV with a list of job experiences."""
    # area adjustment factor for plot circles
    area_adj = 0.65

    fig, legend = make_jobs_plot(parser(csv), area_adj)
    try:
        fig.savefig(image, bbox_extra_artists=(legend,), bbox_inches="tight")
        print("The image has been saved as", image)
    except OSError as err:
        die(f"Cannot create the plot: {err}")


if __name__ == "__main__":
    main()
