# Makefile for generating the curriculum vitae in pdf format
# Copyright (C) 2017 by Davide Madrisan <davide.madrisan@gmail.com>

srcdir = .

CV = dmadrisan_cv_en.tex
EXPERIENCES = experiences.csv
PLOT = images/experiences.png

all: plot pdf

plot: /usr/bin/python3 /usr/bin/latex
	@echo "Generating the plot png image..."
	/usr/bin/python3 -m venv ./pyvenv && \
	./pyvenv/bin/pip3 install matplotlib numpy scipy && \
	./pyvenv/bin/python3 ./scripts/plot-experiences.py \
	    --csv=$(srcdir)/$(EXPERIENCES) \
	    --image=$(srcdir)/$(PLOT)

pdf-only: /usr/bin/pdftex
	@echo "Generating the cv in pdf format..."
	/usr/bin/pdftex $(srcdir)/$(CV)

pdf: plot pdf-only

clean:
	rm -f *.log *.pdf
