# kmr_standardizer

A regex-based Kurdish Kurmanji text standardizer that applies orthographic rules from [Rêbara Rastnivîsînê by Weqfa Mezopotamya](https://mezopirtuk.com/tr/rebera-rastnivisine-p10) to normalize text into standard written form.

## Install
```
pip install  git+https://github.com/cikay/kmr_standardizer.git
```

## Usage and Features

**Preposition standardization**
- di ... de → di ... da
```py
>>> import kmr_standardizer
>>> text = "Berî çend salan, muzîka kurdî bi piranî di nav malbatan de dihat guhdarîkirin."
>>> result = kmr_standardizer.standardize(text)
>>> result
'Berî çend salan, muzîka kurdî bi piranî di nav malbatan da dihat guhdarîkirin.'
>>>
```

- derbarê ... de → derbarê ... da

```py
>>> text = "derbarê edebiyata Kurdî de"
>>> result = kmr_standardizer.standardize(text)
>>> result
'derbarê edebiyata Kurdî da'
>>>
```

- der barê ... de → der barê ... da
```py
>>> text = "Hestên neteweyî û helwesta axêverên wî zimanî ya der barê zimanê wan de"
>>> result = kmr_standardizer.standardize(text)
>>> result
'Hestên neteweyî û helwesta axêverên wî zimanî ya der barê zimanê wan da'
>>>
```

- derheqê ... de → derheqê ... da
```py
>>> text = "Tişta gelekî balkêş a derheqê babilîyan de ev e ji bo hesabên xwe tablo çêdikirin."
>>> result = kmr_standardizer.standardize(text)
>>> result
'Tişta gelekî balkêş a derheqê babilîyan da ev e ji bo hesabên xwe tablo çêdikirin.'
>>>
```

- der heqê ... de → der heqê ... da

```py
>>> text = "Lê bi kurtasî be jî, ez dixwazim dîsan çend gotinan der heqê vê yekê de bibêjim."
>>> result = kmr_standardizer.standardize(text)
>>> result
'Lê bi kurtasî be jî, ez dixwazim dîsan çend gotinan der heqê vê yekê da bibêjim.'
>>>
```


- tê de → tê da

```py
>>> text = "bi her awayî ve raboriya me jî tê de ye"
>>> result = kmr_standardizer.standardize(text)
>>> result
'bi her awayî ve raboriya me jî tê da ye'
>>>
```


- ji ... re → ji ... ra

```py
>>> text = "Carinan wekî jibîrbûyî bixuyên jî, lê ew di binhiş de bi cih bûne û wan ji xwe re hêlîna xwe çêkiriye"
>>> result = kmr_standardizer.standardize(text)
>>> result
'Carinan wekî jibîrbûyî bixuyên jî, lê ew di binhiş da bi cih bûne û wan ji xwe ra hêlîna xwe çêkiriye'
>>>
```


- bi ... re → bi ... ra

```py
>>> text = "Carinan li ser teşeyê peyvekê pirs bi mirov re çêdibin bê çima wisan lê hatiye û ketiye rewşeke din."
>>> result = kmr_standardizer.standardize(text)
>>> result
'Carinan li ser teşeyê peyvekê pirs bi mirov ra çêdibin bê çima wisan lê hatiye û ketiye rewşeke din.'
>>>
```


- di ... re → di ... ra
```py
>>> text = "Meseleya zimanî, meseleyeke wisan e ku di ser hemû partî û rêxistinan re ye."
>>> result = kmr_standardizer.standardize(text)
>>> result
'Meseleya zimanî, meseleyeke wisan e ku di ser hemû partî û rêxistinan ra ye.'
>>>
```


- jê re → jê ra

```py
>>> text = "Ev jî kêşeyeke me ya din e û divê jê re jî çareseriyeke rast bê dîtin."
>>> result = kmr_standardizer.standardize(text)
>>> result
'Ev jî kêşeyeke me ya din e û divê jê ra jî çareseriyeke rast bê dîtin.'
>>>
```


- pê re → pê ra

```py
>>> text = "pê ra jidestçûna çanda kurdî jî"
>>> result = kmr_standardizer.standardize(text)
>>> result
'pê ra jidestçûna çanda kurdî jî'
>>>
```


- tê re → tê re

```py
>>> text = "Tevî ku serêşî û wextê wê yê rêwingiyê hindiktir e jî tê re neçûm."
>>> result = kmr_standardizer.standardize(text)
>>> result
'Tevî ku serêşî û wextê wê yê rêwingiyê hindiktir e jî tê ra neçûm.'
>>>
```


## Contribution

```bash
git clone https://github.com/cikay/kmr_standardizer.git
cd kmr_standardizer
pipenv install --dev
```

### Running Tests

```bash
pipenv run pytest tests/ -v
```
