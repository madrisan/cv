from matplotlib.font_manager import FontProperties
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

# Jobs:
job_list = [
   'Development - C/C++/Java',
   'Development - Linux System',
   'Development - Math',
   'Development - Python',
   'Development - Shell Scripts',
   'Development - TeX',
   'Development - Web',
   'Linux System - Administration',
   'Linux System - DevOps',
   'Monitoring',
   'LAN/WAN Networking'
]

def t(job):
    return job_list.index(job)

jobs = [
   { 'year_start': [1995,  9], 'year_end': [1996,  6], 'type': 'Development - Math' },
   # University - Teoria delle Macchine Calcolatrici
   { 'year_start': [1996,  4], 'year_end': [1996, 11], 'type': 'Development - C/C++/Java' },
   { 'year_start': [1996,  6], 'year_end': [1999,  6], 'type': 'Development - TeX' },
   # University - Courses
   { 'year_start': [1997,  2], 'year_end': [1997,  7], 'type': 'Development - Math' },
   { 'year_start': [1997,  2], 'year_end': [1997,  9], 'type': 'Development - Math' },
   # University - Thesis
   { 'year_start': [1998,  6], 'year_end': [1999,  6], 'type': 'Development - Math' },
   # Accademia delle Scienze Torino
   { 'year_start': [1998, 10], 'year_end': [1999,  2], 'type': 'Development - TeX' },
   # University - Algebra Computazionale
   { 'year_start': [1998,  4], 'year_end': [1998,  5], 'type': 'Development - Math' },
   # Jobs as Networking Engineer
   { 'year_start': [1999, 10], 'year_end': [2004,  8], 'type': 'LAN/WAN Networking' },
   # Atlanet - Skeleton
   { 'year_start': [2001, 11], 'year_end': [2002,  8], 'type': 'Development - Shell Scripts' },
   { 'year_start': [2002,  2], 'year_end': [2002,  3], 'type': 'Development - C/C++/Java' },
   # Atlanet - Cisco like documentation
   { 'year_start': [2002,  4], 'year_end': [2002,  5], 'type': 'Development - TeX' },
   { 'year_start': [2003,  3], 'year_end': [2003,  8], 'type': 'Monitoring' },
   # QiLinux
   { 'year_start': [2004,  9], 'year_end': [2006, 12], 'type': 'Development - Linux System' },
   { 'year_start': [2006,  9], 'year_end': [2006, 10], 'type': 'Development - C/C++/Java' },
   # QiLinux web site
   { 'year_start': [2006,  9], 'year_end': [2006, 10], 'type': 'Development - Web' },
   # QiLinux/Openmamba autospec - start
   { 'year_start': [2004,  8], 'year_end': [2006,  6], 'type': 'Development - Shell Scripts' },
   { 'year_start': [2006, 11], 'year_end': [2007,  6], 'type': 'Development - Shell Scripts' },
   { 'year_start': [2007,  9], 'year_end': [2008,  1], 'type': 'Development - Shell Scripts' },
   { 'year_start': [2008,  5], 'year_end': [2008, 12], 'type': 'Development - Shell Scripts' },
   { 'year_start': [2009, 10], 'year_end': [2009, 11], 'type': 'Development - Shell Scripts' },
   { 'year_start': [2010,  1], 'year_end': [2010,  3], 'type': 'Development - Shell Scripts' },
   { 'year_start': [2010, 10], 'year_end': [2011,  4], 'type': 'Development - Shell Scripts' },
   { 'year_start': [2011, 12], 'year_end': [2012, 12], 'type': 'Development - Shell Scripts' },
   { 'year_start': [2014, 11], 'year_end': [2014, 12], 'type': 'Development - Shell Scripts' },
   # QiLinux/Openmamba autospec - end
   # QiLinux - disk partitioner
   { 'year_start': [2005,  3], 'year_end': [2005,  4], 'type': 'Development - Python' },
   # IBM Italy - Turin
   { 'year_start': [2007,  1], 'year_end': [2008,  5], 'type': 'Linux System - Administration' },
   # Openmamba dev
   { 'year_start': [2007,  3], 'year_end': [2007,  4], 'type': 'Development - Linux System' },
   { 'year_start': [2007,  8], 'year_end': [2007,  9], 'type': 'Development - Linux System' },
   { 'year_start': [2008,  1], 'year_end': [2008,  2], 'type': 'Development - Linux System' },
   { 'year_start': [2008,  6], 'year_end': [2008,  7], 'type': 'Development - Linux System' },
   { 'year_start': [2008, 11], 'year_end': [2008, 12], 'type': 'Development - Linux System' },
   { 'year_start': [2009,  4], 'year_end': [2009,  5], 'type': 'Development - Linux System' },
   { 'year_start': [2009,  9], 'year_end': [2009, 10], 'type': 'Development - Linux System' },
   { 'year_start': [2010,  3], 'year_end': [2010,  4], 'type': 'Development - Linux System' },
   { 'year_start': [2010,  8], 'year_end': [2010,  9], 'type': 'Development - Linux System' },
   { 'year_start': [2011,  1], 'year_end': [2011,  2], 'type': 'Development - Linux System' },
   { 'year_start': [2011,  6], 'year_end': [2011,  7], 'type': 'Development - Linux System' },
   { 'year_start': [2011, 11], 'year_end': [2011, 12], 'type': 'Development - Linux System' },
   { 'year_start': [2012,  4], 'year_end': [2012,  5], 'type': 'Development - Linux System' },
   { 'year_start': [2012,  9], 'year_end': [2012, 10], 'type': 'Development - Linux System' },
   #
   { 'year_start': [2008,  7], 'year_end': [2008, 10], 'type': 'Development - C/C++/Java' },
   { 'year_start': [2008, 11], 'year_end': [2011,  9], 'type': 'Linux System - Administration' },
   # Refont cv in TeX
   { 'year_start': [2010,  3], 'year_end': [2010,  3], 'type': 'Development - TeX' },
   { 'year_start': [2011, 10], 'year_end': [2014,  6], 'type': 'Monitoring' },
   # Scripts PHP IBM
   { 'year_start': [2011, 10], 'year_end': [2012,  2], 'type': 'Development - Web' },
   # Development on Rasberry Pi - System
   { 'year_start': [2013,  3], 'year_end': [2013,  6], 'type': 'Development - Linux System' },
   # Development on Rasberry Pi - XBMC pilot
   { 'year_start': [2013,  4], 'year_end': [2013,  7], 'type': 'Development - Python' },
   # Nagios PLugins for Linux
   { 'year_start': [2014,  2], 'year_end': [2015, 12], 'type': 'Development - C/C++/Java' },
   { 'year_start': [2014,  7], 'year_end': [2016,  8], 'type': 'Linux System - DevOps' },
   # Sopra-Steria
   { 'year_start': [2014,  9], 'year_end': [2015, 10], 'type': 'Development - Shell Scripts' },
   # Base SUD Networking
   { 'year_start': [2014, 11], 'year_end': [2015,  2], 'type': 'LAN/WAN Networking' },
   { 'year_start': [2015,  1], 'year_end': [2015,  4], 'type': 'Monitoring' },
   # MOOC C++
   { 'year_start': [2015,  4], 'year_end': [2015,  5], 'type': 'Development - C/C++/Java' },
   # MOOCs Java
   { 'year_start': [2015,  6], 'year_end': [2015,  6], 'type': 'Development - C/C++/Java' },
   # MOOC HTML5
   { 'year_start': [2015,  7], 'year_end': [2015,  8], 'type': 'Development - Web' },
   # PyOOCS
   { 'year_start': [2015,  9], 'year_end': [2016,  1], 'type': 'Development - Python' },
   # System tools
   { 'year_start': [2015, 10], 'year_end': [2015, 11], 'type': 'Development - Python' },
   # OpenMamba - Data Analisys tools
   { 'year_start': [2015, 11], 'year_end': [2015, 12], 'type': 'Development - Linux System' },
   # Full Stack Web Specialization
   { 'year_start': [2015, 12], 'year_end': [2016,  6], 'type': 'Development - Web' },
   # jQuery, TypeScript, Angular.js
   { 'year_start': [2016,  2], 'year_end': [2016,  3], 'type': 'Development - Web' },
   { 'year_start': [2016,  5], 'year_end': [2016,  6], 'type': 'Development - Web' },
   # MOOC Dynamic Systems and Chaos
   { 'year_start': [2016,  7], 'year_end': [2016,  8], 'type': 'Development - Math' },
   # MOOCs JavaScripts
   { 'year_start': [2016,  7], 'year_end': [2016,  8], 'type': 'Development - Web' }
]

color_list = plt.cm.Paired(np.linspace(0, 1, len(job_list)))
def c(job):
   return color_list[t(job)]

bullet_factor = 90

months = []
jobtype = []
year = []
colors = []

for job in jobs:
    ystart = job['year_start'][0] + job['year_start'][1] / 12.0
    yend = job['year_end'][0] + job['year_end'][1] / 12.0

    delta = yend - ystart
    yhalf = ystart + delta / 2.0

    year.append(yhalf)
    months.append(12*delta + 1);
    jobtype.append(t(job['type']))
    colors.append(c(job['type']))

fig = plt.figure(1)

ax = fig.add_subplot(111)
ax.scatter(x=year, y=jobtype, s=[m * bullet_factor for m in months],
           c=colors, alpha=0.5)

# Add axis labels
ax.set_xlabel('Year')
ax.set_ylabel('Job Typology')
ax.set_title('Job History')
ax.set_xlim([1995, 2020])

# Add grid
yticks = range(0, len(job_list), 2)
ax.set_yticks(yticks)
ax.set_yticklabels([''] * len(yticks))
ax.grid('on')

def textlabel(x, y, text):
    ax.text(x, y, text, style='italic', color='gray', fontsize=10)
            #, bbox={'facecolor':'red', 'alpha':0.5, 'pad':6})

textlabel(1995.4,  3.1, 'Development')
textlabel(1995.4,  7.4, 'Linux system')
textlabel(1995.4,  8.9, 'Monitoring')
textlabel(1995.4, 10.3, 'Networking')

# Add a legend
handles = [mpatches.Patch(color=c(job),
                          label=job, alpha=0.8) for job in job_list]
lgd = ax.legend(reversed(handles), reversed(job_list),
                loc='upper right', bbox_to_anchor=(1.55, 0.8),
                prop={'size': 12})

fig.savefig('../images/experiences.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
