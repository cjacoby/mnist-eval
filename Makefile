DATA_DIR := data
OUTPUT_ROOT := output
MODEL_ROOT := $(OUTPUT_ROOT)/model
FEAT_DIR := $(OUTPUT_ROOT)/features

SELECTED_MODEL := ./classifier/cnn.py
MODEL_DIR := $(MODEL_ROOT)/$(basename $(notdir $(SELECTED_MODEL)))

PYTHON := python


all: features train evaluate report

$(FEAT_DIR)/train.json $(FEAT_DIR)/test.json:
	$(PYTHON) process/extract_features.py $(DATA_DIR)

features: $(FEAT_DIR)/train.json $(FEAT_DIR)/test.json

train: $(FEAT_DIR)/train.json
	$(PYTHON) $(SELECTED_MODEL) train
	touch $<

evaluate: $(FEAT_DIR)/test.json $(MODEL_DIR)/model.pkl
	$(PYTHON) $(SELECTED_MODEL) eval

report: $(MODEL_DIR)/results.json
	$(PYTHON) process/report_results.py

test:
	@}echo "Data Dir: $(DATA_DIR)"
	@echo "Output Root: $(OUTPUT_ROOT)"
	@echo "Model Root: $(MODEL_ROOT)"
	@echo "Feature Dir: $(FEAT_DIR)"
	@echo "Selected Model: $(SELECTED_MODEL)"
	@echo "Model Dir: $(MODEL_DIR)"
	py.test

clean:
	rm -f $(FEAT_DIR)/.sentinel $(MODEL_DIR)/*

