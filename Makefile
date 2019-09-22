# Makefile for generating the curriculum vitae in pdf format
# Copyright (C) 2017 by Davide Madrisan <davide.madrisan@gmail.com>

srcdir = .

CV = dmadrisan_cv_en.tex
EXPERIENCES = experiences.csv
PLOT = images/experiences.png

FONTAWESOME = fontawesome.tex

DOCKER = $(shell command -v docker 2>/dev/null)
ifndef DOCKER
        $(error "please install docker-ce or adjust the PATH environment")
endif

IMAGE = cv
PWD = $(shell pwd)
VOLUMES = -v $(PWD):/appl

ifdef QUIET
        DOCKER_OPTS += --quiet
endif

all: pdf

image: $(DOCKER)
	@sudo $(DOCKER) build -t $(IMAGE) $(DOCKER_OPTS) docker

fontawesome: image
	@echo "Generating the fontawesome pdf..."
	sudo $(DOCKER) run $(VOLUMES) --rm $(IMAGE) \
	    /usr/bin/pdftex $(srcdir)/$(FONTAWESOME)

pdf-only: image
	@echo "Generating the cv in pdf format..."
	sudo $(DOCKER) run $(VOLUMES) --rm $(IMAGE) \
	    /usr/bin/pdftex $(srcdir)/$(CV)

plot: image
	@echo "Generating the plot png image..."
	sudo $(DOCKER) run $(VOLUMES) --rm $(IMAGE) \
	    /usr/bin/python3 /appl/scripts/plot-experiences.py \
	        --csv=$(srcdir)/$(EXPERIENCES) \
	        --image=$(srcdir)/$(PLOT)

pdf: plot pdf-only

clean:
	rm -f *.log *.pdf
