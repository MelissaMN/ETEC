namespace CadastroEventosApp.Models;

public class Evento
{
    public string Nome { get; set; } = string.Empty;
    public DateTime DataInicio { get; set; } = DateTime.Today;
    public DateTime DataTermino { get; set; } = DateTime.Today.AddDays(1);
    public int NumeroParticipantes { get; set; }
    public string Local { get; set; } = string.Empty;
    public decimal CustoPorParticipante { get; set; }

    public TimeSpan Duracao
    {
        get
        {
            return DataTermino >= DataInicio
                ? DataTermino - DataInicio
                : TimeSpan.Zero;
        }
    }

    public int DuracaoEmDias => Duracao.Days;

    public decimal CustoTotal => NumeroParticipantes * CustoPorParticipante;
}
