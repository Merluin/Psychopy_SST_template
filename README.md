# Stop Signal Task (SST) Repository

This repository contains all necessary resources for setting up and running the Stop Signal Task (SST), a behavioral task used to study response inhibition and control. It includes a PsychoPy3 implementation of the task and an R program to compute the Stop Signal Reaction Time (SSRT) based on the task data. Note that the task and preprocessing are done according to verbruggen et al., 2019.

## Repository Structure
- **PsychoPy3 SST Task**: Contains the PsychoPy3 scripts for running the SST.
- **R Program for SSRT**: Includes R scripts for calculating the SSRT from the experiment data.

## SST Task Overview
The Stop Signal Task involves presenting participants with Go trials where they must respond quickly to a stimulus, and Stop trials where they must inhibit their response upon seeing a stop signal. The task dynamically adjusts the difficulty of stopping based on individual performance to calculate the SSRT.

### Task Details
- **Initial Stop Signal Delay (dynamic SSD)**: 150 ms from go signal offset, adjustable between 50 ms and 650 ms.
- **Stimuli**: Green arrows indicating the response direction.
- **Stop Signal**: "XX" presented after a variable delay.

## Requirements
- **For PsychoPy Task**:
  - PsychoPy v2022.1.4
- **For R Program**:
  - R (latest version recommended)

## Installation

### PsychoPy Task
1. Ensure PsychoPy v2022.1.4 is installed on your system.
2. Clone this repository or download the PsychoPy folder.
3. Navigate to the `PsychoPy3 SST Task` folder.
4. Run the script `SST.psyexp` using PsychoPy.

### R Program
1. Install R from [CRAN](https://cran.r-project.org/).
2. Clone this repository or download the R Program folder.
3. Open and run the scripts in the `R Program for SSRT` folder to compute SSRT from your data.

## Customization
- The PsychoPy task parameters can be customized, such as changing the inter-stimulus intervals or response keys.
- The R scripts can be modified to accommodate different data structures or additional analyses.

## Contact Information
For any queries regarding the implementation or modifications, please contact:
- Thomas Quettier - [thomas.quettier2@unibo.it](mailto:thomas.quettier2@unibo.it)

## References
Verbruggen, F., Aron, A. R., Band, G. P., Beste, C., Bissett, P. G., Brockett, A. T., ... & Boehler, C. N. (2019). A consensus guide to capturing the ability to inhibit actions and impulsive behaviors in the stop-signal task. *eLife*, 8, e46323. [Link to paper](https://doi.org/10.7554/eLife.46323)

## Additional Note:
While not legally binding, the author would appreciate an acknowledgment or citation
where possible if this software is used in the development of new software, publications,
or research. For citation guidelines, please refer to the CITATION file in this repository.
## Collaborative Contributions

For collaborators contributing to this repository, please prefix your commit messages with appropriate tags for efficient tracking and management:
- **BF**: Bug Fix - for resolving errors or issues in existing code.
- **FF**: Feature Fix - for fixes to unreleased code features.
- **RF**: Refactoring - for code structure or design modifications.
- **NF**: New Feature - for introducing new functionalities.
- **ENH**: Enhancement - for improvements to existing features or code.
- **DOC**: Documentation - for updates or additions to project documentation.
- **TEST**: Testing - for adding new tests or modifying existing ones. 

Your cooperation and adherence to these guidelines help maintain the quality and integrity of our project. 
