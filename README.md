# kmr_standardizer

A regex-based Kurdish Kurmanji text standardizer that applies orthographic rules from [Rêbara Rastnivîsînê by Weqfa Mezopotamya](https://mezopirtuk.com/tr/rebera-rastnivisine-p10) to normalize text into standard written form.

## Install
```
pip install  git+https://github.com/cikay/kmr_standardizer.git
```

## Usage

```python
import kmr_standardizer

text = "Berî çend salan, muzîka kurdî bi piranî di nav malbatan de dihat guhdarîkirin."
result = kmr_standardizer.standardize(text)
# "Berî çend salan, muzîka kurdî bi piranî di nav malbatan da dihat guhdarîkirin."
```

## Features

**Preposition standardization**
- `di ... de` → `di ... da` (e.g., *di mal de* → *di mal da*)
- `derbarê ... de` → `derbarê ... da` (e.g., *derbarê vê mijarê de* → *derbarê vê mijarê da*)
- `der barê ... de` → `der barê ... da` (e.g., *der barê vê mijarê de* → *derbarê vê mijarê da*)
- `derheqê ... de` → `derheqê ... da` (e.g., *derheqê vê mijarê de* → *derheqê vê mijarê da*)
- `der heqê ... de` → `der heqê ... da` (e.g., *der heqê vê mijarê de* → *der heqê vê mijarê da*)
- `tê de` → `tê da` (e.g., *tê de ew peyv jî heye* → *tê da ew peyv jî heye*)
- `ji ... re` → `ji ... ra` (e.g., *ji min re* → *ji min ra*)
- `bi ... re` → `bi ... ra` (e.g., *bi min re* → *bi min ra*)
- `di ... re` → `di ... ra` (e.g., *di bin re* → *di bin ra*)
- `jê re` → `jê ra` (e.g., *Min jê re got* → *Min jê ra got*)
- `pê re` → `pê ra` (e.g., *Ew jî pê re hat* → *Ew jî pê ra hat*)
- `tê re` → `tê re` (e.g., *tê re derbas bûn* → *tê re derbas bûn*)


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
