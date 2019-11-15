# Makefile for generating the curriculum vitae in pdf format
# Copyright (C) 2017-2019 by Davide Madrisan <davide.madrisan@gmail.com>

# Works with docker-ce and podman with or without podman-docker

srcdir = .

CV = dmadrisan_cv_en.tex
EXPERIENCES = experiences.csv
PLOT = images/experiences.png

FONTAWESOME = fontawesome.tex

DOCKER = $(shell command -v docker 2>/dev/null)
PODMAN = $(shell command -v podman 2>/dev/null)
ifneq ($(PODMAN),)
    CONTAINER_ENGINE = $(PODMAN)
else ifneq ($(DOCKER),)
    CONTAINER_ENGINE = $(DOCKER)
else
    $(error "please install docker-ce or podman or adjust the PATH environment")
endif

IMAGE = cv
PWD = $(shell pwd)
VOLUMES = -v $(PWD):/appl:Z

ifdef QUIET
        OPTS += --quiet
endif

all: pdf

image: $(CONTAINER_ENGINE)
	@sudo $(CONTAINER_ENGINE) build -t $(IMAGE) $(OPTS) docker

fontawesome: image
	@echo "Generating the fontawesome pdf..."
	sudo $(CONTAINER_ENGINE) run $(VOLUMES) --rm $(IMAGE) \
	    /usr/bin/pdftex $(srcdir)/$(FONTAWESOME)

pdf-only: image
	@echo "Generating the cv in pdf format..."
	sudo $(CONTAINER_ENGINE) run $(VOLUMES) --rm $(IMAGE) \
	    /usr/bin/pdftex $(srcdir)/$(CV)

plot: image
	@echo "Generating the plot png image..."
	sudo $(CONTAINER_ENGINE) run $(VOLUMES) --rm $(IMAGE) \
	    /usr/bin/python3 /appl/scripts/plot-experiences.py \
	        --csv=$(srcdir)/$(EXPERIENCES) \
	        --image=$(srcdir)/$(PLOT)

pdf: plot pdf-only

clean:
	rm -f *.log *.pdf
