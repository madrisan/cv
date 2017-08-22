# Makefile for generating the curriculum vitae in pdf format
# Copyright (C) 2017 by Davide Madrisan <davide.madrisan@gmail.com>

srcdir = .

CV = dmadrisan_cv_en.tex
EXPERIENCES = scripts/experiences.csv
PLOT = images/experiences.png

all: plot pdf

plot:
	@echo "Generating the plot png image..."
	./scripts/plot-experiences.py      \
	    --csv=$(srcdir)/$(EXPERIENCES) \
	    --image=$(srcdir)/$(PLOT)

pdf: plot
	@echo "Generating the cv in pdf format..."
	/usr/bin/pdftex $(srcdir)/$(CV)
