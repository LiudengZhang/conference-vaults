# torch (R)

**PyTorch in R** — a CRAN package providing R-native tensor operations and neural-network APIs on top of libtorch (the C++ backend underlying PyTorch), with GPU acceleration. No Python dependency — torch ships its own libtorch binaries. The GBCC2025 talk uses it as the substrate for a deep-learning epigenetic-clock methodology.

- **Maintainer:** Tomasz Kalinowski (Posit) — `tomasz@posit.co`
- **Authors:** Daniel Falbel, Javier Luraschi, Tomasz Kalinowski, Dmitriy Selivanov, Athos Damiani, Christophe Regouby, Krzysztof Joachimiak, Hamada S. Badr, Sebastian Fischer, Maximilian Pichler, RStudio
- **CRAN:** [torch on CRAN](https://cran.r-project.org/package=torch); pkgdown site: [torch.mlverse.org](https://torch.mlverse.org/)
- **Source:** [github.com/mlverse/torch](https://github.com/mlverse/torch)
- **License:** MIT
- **Status at GBCC2025:** external (CRAN, not Bioconductor); methods talk uses torch as the deep-learning substrate

## Talk at GBCC2025

- **Speaker:** Jamie Park
- **Day / session:** Day 2 — Oral Session 2A
- **Talk title:** "Leveraging Deep Learning with torch in R for Next-Generation Epigenetic Clock Development"
- **Slides:** *to verify after publish*
- **Video:** [GBCC2025 playlist](https://www.youtube.com/playlist?list=PLdl4u5ZRDMQTJ0O_FIO9ayqaUDfnMo4-4)
- **Abstract / schedule:** [GBCC2025 program](https://gbcc2025.bioconductor.org/program/scientific_program/)

## What it does

torch gives R users PyTorch-equivalent functionality without requiring Python: tensor algebra, autograd, `nn_module` definitions, optimizers, dataloaders, GPU placement (CUDA / MPS), and JIT-traced model export. Because the backend is libtorch (the same C++ library PyTorch wraps), models trained in R-torch are bit-compatible with PyTorch checkpoints. For Bioconductor-adjacent users, this means deep-learning methods can be developed alongside SE / SCE workflows without language-switching.

## How it works

**Core idea.** torch binds R directly to libtorch — the same C++ library PyTorch wraps — via Rcpp, so R code calls into the identical tensor/autograd kernels Python uses, with no Python interpreter in the stack and no `reticulate` bridge.

**Inputs / outputs.** Input is R-native data (vectors, matrices, arrays, R6-defined `dataset` objects). Output is `torch_tensor` objects living on CPU or GPU, `nn_module` instances with learnable parameters, fitted weights serializable to libtorch state-dict format, and predictions returned as R arrays.

**Key innovation.** A Python-free PyTorch port: libtorch binaries ship with the package (no Python install required), and because the kernels are the same C++ library PyTorch uses, weights are interchangeable with PyTorch checkpoints — making R a first-class language for deep-learning method development rather than a Python wrapper.

**Parameters / API surface worth knowing.**
- `torch_tensor()`, `torch_randn()`, `torch_zeros()` — tensor constructors with `device = "cuda"` / `"mps"` / `"cpu"` placement.
- `nn_module()` — R6-style class for defining custom network architectures with `forward()` methods.
- `optim_adam()`, `optim_sgd()`, `nnf_*` functional API — optimizers and stateless ops mirroring PyTorch's `torch.nn.functional`.
- `dataset()` + `dataloader()` — coroutine-based (`coro`) iterator infrastructure for batching.
- Autograd: `tensor$backward()` and `with_no_grad()` for gradient control.

**Canonical example.** From the torch documentation: define an `nn_module` subclass with `initialize()` declaring layers and `forward()` defining the forward pass; instantiate, move to GPU with `model$to(device = "cuda")`, loop over a `dataloader`, call `loss$backward()` and `optimizer$step()` — the idioms are line-for-line equivalent to PyTorch. Park's GBCC talk uses this skeleton to train an epigenetic-clock network on methylation arrays from R.

## What the GBCC talk contributes

Park's talk frames torch as the *substrate*; the contribution is a deep-learning architecture for epigenetic-clock estimation (predicting biological age from DNA-methylation arrays). Epigenetic clocks (Horvath, GrimAge, PhenoAge, DunedinPACE) are increasingly used as biomarkers in oncology, aging, and clinical trials, and the field has been moving from penalized-regression (elastic net) clocks to deep-learning variants — Park's work sits squarely in that transition.

## Where it fits in the corpus

- **AACR 2026:** axes = bioinfo-tools + clinical-trials (epigenetic clocks are biomarker / clinical-trial endpoints; cross-language deep-learning is increasingly load-bearing)
- **SpectriPy** ([entry](../../eurobioc-2025/tools/spectripy.md)) and **SpatialData** ([entry](../../eurobioc-2025/tools/spatialdata.md)) — sister cross-language stories: torch is the R-side analog to PyTorch, SpectriPy / SpatialData are R↔Python interop bridges. Together they describe the polyglot direction the Bioc community is heading
- **iscream** ([entry](iscream.md)) — Park's clock would consume per-region methylation matrices; iscream is the fast assembler of those matrices
- **EuroBioC 2025:** not presented
- **Nextflow Summit 2026:** not mentioned (different ecosystem)

## Notes

torch itself is mature (v0.17.0); the GBCC novelty is its application — a next-generation epigenetic clock built in R-torch. The talk is interesting both as a concrete clinical-biomarker contribution and as evidence that deep-learning methods development is now feasible inside the R / Bioconductor ecosystem without forcing a Python migration.
