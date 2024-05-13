#' Preprocess Data and Calculate SSRT Metrics
#'
#' This function preprocesses a given dataset (expected to be in .csv format) and computes various Stop-Signal Reaction Time (SSRT) metrics. 
#' It is specifically tailored for experiments where response times to go/no-go tasks are measured, and differentiates between 
#' successful and unsuccessful stop trials, while also adjusting for go trials omission.
#'
#' @param data A dataframe containing the experimental data. Each row represents a trial.
#'
#' The function performs several key operations:
#' 1. Data Filtering and Transformation:
#'    - Converts several columns to factor type based on the role they play in the experiment (e.g., participant IDs, file names, keys).
#'    - Calculates real stop-signal delays (SSD) by capturing time differences between stop and go signals, adjusting for trials with no stop signal.
#'    - Filters and modifies data based on specific experimental conditions (like the repetition number of blocks and trial number within blocks).
#'
#' 2. Reaction Time (RT) Analysis:
#'    - Calculates descriptive statistics (mean, min, max, SD) for reaction times, both for all go trials and for correct go trials only.
#'
#' 3. Stop-Signal Delay (SSD) Analysis:
#'    - Computes mean and standard deviation of SSD for stop trials.
#'
#' 4. Stop Trials Analysis:
#'    - Aggregates data to count total, successful, and unsuccessful stop trials.
#'    - Calculates inhibition rates and probabilities of responding under stop-signal conditions.
#'
#' 5. Go Trials Analysis:
#'    - Calculates accuracy and response metrics for go trials, considering both omissions and premature responses.
#'
#' 6. SSRT Calculation:
#'    - Determines the SSRT by taking the nth reaction time (where n is determined by stop-signal response probability) and subtracting the mean SSD.
#'
#' 7. Summarizing and Returning Data:
#'    - Prepares a detailed summary table for each subject, encompassing all computed metrics and descriptive statistics rounded to three decimal places.
#'
#' @return A dataframe containing SSRT metrics and other statistical summaries for each subject.
#'
#' @export
#'
#' Example usage:
#' preprocess_data <- preprocessing(read.csv("path_to_your_data.csv"))
#'
preprocessing <- function(data)
{
  # Select relevant data and apply necessary filters
  data <- data %>%
    filter(Loop_blocchi.thisRepN >= 0) %>%  # Include only data from blocks that have been repeated
    mutate(
      subject = as.factor(participant),  # Convert participant ID to a factor (chosen during experiment dialog box)
      go_file = as.factor(go_file),  # Convert filename of 'go' trial picture to a factor (refer to conditions.xlsx for details)
      stop_file = as.factor(stop_file),  # Convert filename of 'stop' trial picture to a factor (refer to conditions.xlsx for details)
      correct_key = as.factor(correct_key),  # Convert correct response key to a factor (refer to conditions.xlsx for details)
      signal = as.factor(signal),  # Categorize trials as 'stop' (1) or 'go' (0)
      SSD = ifelse(signal == 0, NA, SSD),  # Calculate the stop-signal delay (SSD), set as NA for 'go' trials
      stop_img.stopped = ifelse(stop_img.stopped == "None", NA, stop_img.stopped),  # Convert 'None' to NA in stop_img.stopped
      go_img.stopped = ifelse(go_img.stopped == "None", NA, go_img.stopped),  # Convert 'None' to NA in go_img.stopped
      SSD.real = round((as.numeric(stop_img.stopped) - as.numeric(go_img.stopped)) * 1000, 0),  # Calculate real SSD, round to milliseconds
      SSD.real = ifelse(signal == 0, NA, SSD.real),  # Set SSD.real to NA for 'go' trials
      response = as.factor(key_resp.keys),  # Convert participant's response key to a factor
      congruent = key_resp.corr,  # Boolean flag indicating if the response was correct (congruent with correct_key)
      premature = premature,  # Flag for premature responses in both stop and go trials
      rt = RT,  # Record participant's reaction time
      bloch = Loop_blocchi.thisRepN + 1,  # Adjust block numbering to start from 1 (data source may begin count from 0)
      trial = loop_trials.thisN + 1  # Adjust trial numbering within each block to start from 1
    ) %>%
    select(  # Select columns to be used in further analysis
      subject, go_file, stop_file, correct_key, signal, SSD, SSD.real, premature,
      bloch, trial,
      response, congruent, rt
    )
  
  
  
  # RT ----
  # Mean and Max RT
  RT <- data %>%
    filter(signal == 0 & response != "None") %>%# eliminate correct stop trial and Go ommission
    summarise(max = max(rt, na.rm = TRUE), # max rt
              min = min(rt, na.rm = TRUE), # min rt
              mean = mean(rt, na.rm = TRUE), # mean rt
              sd = sd(rt, na.rm = TRUE)) # sd rt
  
  # Mean RT Only for Correct
  RT.Cor <- data %>%
    filter(signal == 0 & response != "None" & congruent == 1) %>% # eliminate correct stop trial and Go ommission
    summarise(max = max(rt, na.rm = TRUE), # max correct rt
              min = min(rt, na.rm = TRUE), # min correct rt
              mean = mean(rt, na.rm = TRUE), # mean correct rt
              sd = sd(rt, na.rm = TRUE)) # sd correct rt
  
  # SSD ----
  SSD <- data %>%
    filter(signal == 1) %>%# eliminate correct stop trial
    summarise(mean = mean(SSD, na.rm = TRUE),# mean correct ssd
              sd = sd(SSD, na.rm = TRUE))# sd correct ssd
  SSD.real <- data %>%
    filter(signal == 1) %>%# eliminate correct stop trial
    summarise(mean = mean(SSD.real, na.rm = TRUE),# mean correct ssd
              sd = sd(SSD.real, na.rm = TRUE))# sd correct ssd
  
  # Stop trials ----
  Stop <- cbind(
    tot <- data %>% # number of stop trials 
      filter(signal == 1 ) %>% 
      summarise(tot = n()),
    cor <- data %>% # Successfull stop trials 
      filter(signal == 1 & response == "None") %>% 
      summarise(Success = n()),
    inc <- data %>% # Unsuccessfull stop trials 
      filter(signal == 1 & response != "None") %>% 
      summarise(Unsuccess = n()),
    choice <- data %>% # choice error in stop trials 
      filter(signal == 1 & response != "None" & congruent == 0) %>% 
      summarise(choice.error = n()),
    pre <- data %>% # precoce response on stop trial
      filter(signal == 1 & premature == 1) %>% 
      summarise(premature = n()), 
    UnsuccessStopMeanReactionTime <- data %>% # Unsuccess Stop Mean Reaction Time on stop trials 
      filter(signal == 1 & response != "None") %>%  
      summarise(USRT = mean(rt, na.rm =TRUE)) 
  ) %>%
    mutate(inhibition.rate = Success/tot, # 
           p_respond = Unsuccess/tot) # p(respond|signal)
  
  
  # sorted RT ----
  sorted_RT<- data %>%
    filter(signal == 0) %>% 
    mutate(go_omission = ifelse(response == "None",1,0),
           rt = ifelse(response == "None",RT$max,rt) # replace go omission with max rt
    ) %>%
    select(rt,go_omission) %>%
    arrange(rt, .by_group = TRUE) %>% # sorting rts
    data.frame()
  
  # Go trials  ----
  Go <- cbind(
    cor <- data %>%
      filter(signal == 0 & congruent == 1) %>% 
      summarise(correct = n()),
    inc <- data %>%
      filter(signal == 0 & congruent == 0 & response != "None") %>% 
      summarise(error = n()),
    omi <- data %>%
      filter(signal == 0 ) %>% 
      mutate(go_omission = ifelse(response == "None",1,0)) %>%
      summarise(omission = sum(go_omission)),
    pre <- data %>%
      filter(signal == 0 & rt <= 0) %>% 
      summarise(premature = n())
  ) %>%
    mutate(tot = correct + error + omission,
           acc = (correct/tot) * 100,
           acc.noOmission = (correct/(tot-omission))*100,
           p_omission = omission/tot,
           p_choice = error/tot)
  # nthRT ----
  
  nthRT <- Go$tot * Stop$p_respond
  
  # SSRT ----
  
  ssrt <- sorted_RT$rt[nthRT] - SSD$mean
  
  # Table ----
  decimal <- 3
  table <- data.frame(
    SubjectName = as.character(data$subject[1]),
    RT.mean = as.numeric(round(RT$mean, decimal)), # RT for all Responses
    RT.sd = as.numeric(round(RT$sd, decimal)),
    RT.min = as.numeric(round(RT$min, decimal)),
    RT.max = as.numeric(round(RT$max, decimal)),
    
    RT.Cor.mean = as.numeric(round(RT.Cor$mean, decimal)), # RTs for correct Go responses (including unsuccessful stop trials)
    RT.Cor.sd = as.numeric(round(RT.Cor$sd, decimal)),
    RT.Cor.min = as.numeric(round(RT.Cor$min, decimal)),
    RT.Cor.max = as.numeric(round(RT.Cor$max, decimal)),
    
    SSD.mean = as.numeric(round(SSD$mean, decimal)),
    SSD.sd = as.numeric(round(SSD$sd, decimal)),
    
    P.respond = as.numeric(round(Stop$p_respond, decimal)),
    
    SSRT = as.numeric(round(ssrt, decimal)),
    
    Go.correct = as.numeric(round(Go$correct, decimal)),
    Go.error = as.numeric(round(Go$error, decimal)),
    Go.p_choice = as.numeric(round(Go$p_choice, decimal)),
    Go.omission = as.numeric(round(Go$omission, decimal)),
    Go.total = as.numeric(round(Go$tot, decimal)),
    Go.accuracy = as.numeric(round(Go$acc, decimal)),
    Go.premature = as.numeric(round(Go$premature, decimal)),
    Go.accuracy.no.omission = as.numeric(round(Go$acc.noOmission, decimal)),
    Go.p_omission = as.numeric(round(Go$p_omission, decimal)),
    
    Stop.Success = as.numeric(round(Stop$Success, decimal)),
    Stop.Unsuccess = as.numeric(round(Stop$Unsuccess, decimal)),
    Stop.total= as.numeric(round(Stop$tot, decimal)),
    Stop.premature = as.numeric(round(Stop$premature, decimal)),
    Stop.usrt = as.numeric(round(Stop$USRT, decimal)),
    Stop.ir = as.numeric(round(Stop$inhibition.rate, decimal)))
  
  return(table)
} #end function 