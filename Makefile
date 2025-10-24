help: ## Show this help message
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

###############################################################################

pytest: ## Run pytest on the tests/ directory
	cd tests && pytest -W ignore::DeprecationWarning

pytest_verbose: ## Run pytest in verbose mode on the tests/ directory
	cd tests && pytest -v -W ignore::DeprecationWarning


##############################################################################

lint: ## Run pyright type checker on src and examples
	pyright ./src/gsp/ ./examples/gsp/

test: lint pytest_verbose ## Run all tests
	@echo "All tests passed!"