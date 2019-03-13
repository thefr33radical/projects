library(esquisse)

if (interactive()) {
  # Launch with:
  esquisse(iris)
  # If in RStudio it will be launched by default in dialog window
  # If not, it will be launched in browser
  
  # change diplay mode with:
  options("esquisse.display.mode" = "viewer")
  # or
  options("esquisse.display.mode" = "browser")
}
