import pandas as pd
import pytest

from src.data_processing import load_and_preprocess_data


@pytest.fixture
def sample_csv_file(tmp_path):
    """
    Cria um arquivo CSV temporário para os testes.
    Usa a fixture 'tmp_path' do pytest para criar um diretório temporário.
    """
    content = "timestamp,value\n2024-01-01 00:00:00,10\n2024-01-01 00:05:00,12"
    file_path = tmp_path / "sample_data.csv"
    file_path.write_text(content)
    return str(file_path)


def test_load_and_preprocess_data(sample_csv_file):
    # Arrange (Organizar): A fixture 'sample_csv_file' já preparou o ambiente.

    # Act (Agir): Chamar a função que está sendo testada.
    df = load_and_preprocess_data(sample_csv_file)

    # Assert (Verificar): Verificar se o resultado é o esperado.
    assert isinstance(df, pd.DataFrame)  # Tipo da variavel df
    assert not df.empty  # Se está vazia
    assert df.index.name == "timestamp"  # Se o nome do indice é timestamp
    assert isinstance(df.index, pd.DatetimeIndex)  # Se o tipo do indice é datetimeindex
    assert "value" in df.columns  # Se existe uma coluna chamada values
    assert not df.isnull().values.any()  # Se algum valor da voluna values é nulo
