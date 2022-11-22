# BatchProcessor System
This system helps to generate batches according to given limitation

------------

## BatchProcessor
- This class helps to split records into the batch for continuous data-delivering systems
- System basically, splits records linearly and group them into batches according to given limitation.
- This system doesn't contain **cache** system because according to given documents, **order of records shouldn't be interrupted.**

## Limitations of Batch Processor
- Maximum size of output record is **1MB**
- Maximum size of output batch is **5MB**
- Maximum number of records in an output batch is **500**
> You can edit these limitations from **Config/ByteSizeConstant.py** file

## Logging of Batch Processor
- Batch Processor system has also logging feature
- After calling or running Batch Processor you can see **BatchProgress.log** file
## Input Record Generator
- This file helps to generate new record list for testing our BatchProcessor system.
- Input Record Generator system uses **random** and **string** libraries for generation process

------------

### Record Parameters

------------


There are 4 different constant parameters for Input Record Generator which they are
1. **RECORD_BYTE_SIZE_START_LIMIT**
(represents the start offset the length of generated strings)
2. **RECORD_BYTE_SIZE_END_LIMIT**
(represents the end offset the length of generated strings)
3. **NUMBER_RECORD_START_LIMIT**
(represents the start offset the number of generated strings(records) in record array)
4. **NUMBER_RECORD_END_LIMIT**
(represents the end offset the number of generated strings(records) in record array)
>You can edit these parameters from **Config/InputRecordConstant.py**


### TestRunner
- TestRunner system basically produce new record with calling Input Record Generator method. After that, it calls batch processor. Lastly, It checks generated batches with given limitation, If any batch or record exceeds limitation, test fails


