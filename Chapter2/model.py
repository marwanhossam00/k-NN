from typing import Optional, Union,Iterable
from collections.abc import Iterator
import datetime


class Sample:
    def __init__(
        self,
        sepal_length:float,
        sepal_width:float,
        petal_length:float,
        petal_width:float,
        species: Optional[str] = None,
    ) -> None:
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species
        self.classification: Optional[str] = None
    
    def __repr__(self) -> str:
        if self.species is None:
            known_unknown = "UnknownSample"
        else:
            known_unknown = "KnownSample"
        if self.classification is None:
            classification = ""
        else:
            classification = f", {self.classification}"
        return(
            f"{known_unknown}("
            f"sepal_length={self.sepal_length}, "
            f"sepal_width={self.sepal_width}, "
            f"petal_length={self.petal_length}, "
            f"petal_width={self.petal_width}, "
            f"species={self.species!r}"
            f"{classification}"
            f")"
        )
    def classify(self, classification:str) -> None:
        self.classification = classification
    
    def matches(self) -> bool:
        return self.species == self.classification

class Hyperparameter:
    """A hyperparameter value and the overall quality of the 
    classification.
    """
    def __init__(self, k:int, training:"TrainingData") -> None:
        self.k = k
        self.data: weakref.ReferenceType["TrainingData"] = weakref.ref(training)
        self.quality:float
    def test(self) -> None:
        training_data: Optional["TrainingData"] = self.data
        if not training_data:
            raise RuntimeError("Broken Weak Reference")
        pass_count, fail_count = 0,0
        for sample in training_data.testing:
            sample.classification = self.classify(sample)
            if sample.matches():
                pass_count += 1
            else:
                fail_count +=1
        self.quality = pass_count / (pass_count + fail_count)
class TrainingData:
    """ A set of training data and testing data with methods to load and
    test the samples
    """
    def __init__(self, name:str)-> None:
        self.name = name
        self.uploaded: datetime.datetime
        self.tested: datetime.datetime
        self.training: list[Sample] = []
        self.testing: list[Sample] = []
        self.tuning: list[Hyperparameter] = []
    
    def load(self, raw_data_source: Iterable[dict[str, str]])-> None:
        """Load and partition raw data."""
        for n, row in enumerate(raw_data_source):
            # filter and extract subsets (chapter 6)
            # create self.training and self.testing subsets
            print("None until Chapter 6")
        
        self.uploaded = datetime.datetime.now(tz=datetime.timezone.utc)
    
    def test(self, parameter:Hyperparameter)->None:
        """Test the hyperparameter value"""
        parameter.test()
        self.tuning.append(parameter)
        self.tested = datetime.datetime.now(tz=datetime.timezone.utc)

    def classify(self,
                 parameter: Hyperparameter,
                 sample: Sample)-> Sample:
        """Classify this Sample."""
        classification = parameter.classify(sample)
        sample.classify(classification)
        return sample