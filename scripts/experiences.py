# List of job categories
job_list = [
   'Development - C/C++/Java',
   'Development - Data Analysis',
   'Development - Linux System',
   'Development - Math',
   'Development - Python',
   'Development - Scala',
   'Development - Shell Scripts',
   'Development - TeX',
   'Development - Web',
   'Linux System - Administration',
   'Linux System - Containers',
   'Linux System - DevOps',
   'Monitoring',
   'LAN/WAN Networking'
]

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
   { 'year_start': [2006,  3], 'year_end': [2006, 12], 'type': 'Development - Web' },
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
   { 'year_start': [2005,  3], 'year_end': [2005,  6], 'type': 'Development - Python' },
   # IBM Italy - Turin
   { 'year_start': [2007,  1], 'year_end': [2008,  5], 'type': 'Linux System - Administration' },
   # Openmamba dev
   { 'year_start': [2007,  1], 'year_end': [2007, 12], 'type': 'Development - Linux System' },
   { 'year_start': [2008,  1], 'year_end': [2008,  6], 'type': 'Development - Linux System' },
   { 'year_start': [2008,  7], 'year_end': [2008, 12], 'type': 'Development - Linux System' },
   { 'year_start': [2009,  1], 'year_end': [2009,  4], 'type': 'Development - Linux System' },
   { 'year_start': [2009,  5], 'year_end': [2009,  8], 'type': 'Development - Linux System' },
   { 'year_start': [2009,  9], 'year_end': [2009, 12], 'type': 'Development - Linux System' },
   { 'year_start': [2010,  1], 'year_end': [2010,  4], 'type': 'Development - Linux System' },
   { 'year_start': [2010,  5], 'year_end': [2010,  8], 'type': 'Development - Linux System' },
   { 'year_start': [2010,  9], 'year_end': [2010, 12], 'type': 'Development - Linux System' },
   { 'year_start': [2011,  1], 'year_end': [2011,  4], 'type': 'Development - Linux System' },
   { 'year_start': [2011,  5], 'year_end': [2011,  8], 'type': 'Development - Linux System' },
   { 'year_start': [2011,  9], 'year_end': [2011, 12], 'type': 'Development - Linux System' },
   { 'year_start': [2012,  1], 'year_end': [2012,  4], 'type': 'Development - Linux System' },
   { 'year_start': [2012,  5], 'year_end': [2012,  8], 'type': 'Development - Linux System' },
   { 'year_start': [2012,  9], 'year_end': [2012, 12], 'type': 'Development - Linux System' },
   { 'year_start': [2015,  3], 'year_end': [2015,  5], 'type': 'Development - Linux System' },
   #
   { 'year_start': [2008,  7], 'year_end': [2008, 10], 'type': 'Development - C/C++/Java' },
   { 'year_start': [2008, 11], 'year_end': [2011,  9], 'type': 'Linux System - Administration' },
   # Rework cv in TeX
   { 'year_start': [2010,  3], 'year_end': [2010,  3], 'type': 'Development - TeX' },
   { 'year_start': [2011, 10], 'year_end': [2014,  6], 'type': 'Monitoring' },
   # Scripts PHP IBM
   { 'year_start': [2011, 10], 'year_end': [2012,  2], 'type': 'Development - Web' },
   # Development on Rasberry Pi - System
   { 'year_start': [2013,  3], 'year_end': [2013,  6], 'type': 'Development - Linux System' },
   # Development on Rasberry Pi - XBMC pilot
   { 'year_start': [2013,  4], 'year_end': [2013,  8], 'type': 'Development - Python' },
   # Nagios PLugins for Linux
   { 'year_start': [2014,  2], 'year_end': [2015, 12], 'type': 'Development - C/C++/Java' },
   # SopraSteria DevOps activities (Docker, SaltStack, Python, rpm/deb packaging: Spacewalk)
   { 'year_start': [2014,  7], 'year_end': [2016, 12], 'type': 'Linux System - DevOps' },
   # Sopra-Steria
   { 'year_start': [2014,  9], 'year_end': [2015, 10], 'type': 'Development - Shell Scripts' },
   # Base SUD Networking
   { 'year_start': [2014, 11], 'year_end': [2015,  2], 'type': 'LAN/WAN Networking' },
   { 'year_start': [2015,  1], 'year_end': [2015,  4], 'type': 'Monitoring' },
   # MOOCs Data Analysis
   { 'year_start': [2014, 10], 'year_end': [2015,  5], 'type': 'Development - Data Analysis' },
   { 'year_start': [2015,  7], 'year_end': [2015,  9], 'type': 'Development - Data Analysis' },
   { 'year_start': [2016,  6], 'year_end': [2016,  7], 'type': 'Development - Data Analysis' },
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
   # openmamba - Data Analysis tools
   { 'year_start': [2014, 11], 'year_end': [2015,  3], 'type': 'Development - Linux System' },
   # Full Stack Web Specialization
   { 'year_start': [2015, 12], 'year_end': [2016,  6], 'type': 'Development - Web' },
   # jQuery, TypeScript, Angular.js, JavaScript, MongoDB, Angular2
   { 'year_start': [2016,  2], 'year_end': [2016, 11], 'type': 'Development - Web' },
   # MOOC Dynamic Systems and Chaos
   { 'year_start': [2016,  7], 'year_end': [2016,  8], 'type': 'Development - Math' },
   # SopraSteria - Python scripts and AWS boto3
   { 'year_start': [2016,  7], 'year_end': [2016, 12], 'type': 'Development - Python' },
   # SopraSteria - build infrastructure using GitLab and Docker)
   { 'year_start': [2016,  7], 'year_end': [2016, 12], 'type': 'Linux System - Containers' },
   # SopraSteria - postinstall framework (SaltStack-based) + GitLab script refont
   { 'year_start': [2016,  6], 'year_end': [2016, 12], 'type': 'Development - Shell Scripts' },
   # Nagios Plugins for Linux v19 + test framework
   { 'year_start': [2016,  9], 'year_end': [2016, 11], 'type': 'Development - C/C++/Java' },
   # MOOCS Paradigms of Computer Programming  (functional programming)
   { 'year_start': [2015,  10], 'year_end': [2016, 1], 'type': 'Development - Scala' },
   # MOOCs Functional Programming in Scala Specialization - Coursera
   { 'year_start': [2016,  10], 'year_end': [2016, 12], 'type': 'Development - Scala' },
]
