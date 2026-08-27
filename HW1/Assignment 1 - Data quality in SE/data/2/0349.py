from ..api import get_many, ApiVersion, int_field, date_field
from datetime import date
from typing import Iterator, List, Optional

class KrajOkresTesty:
    """ Celkový (kumulativní) počet provedených testů podle krajů a okresů ČR

    Datová sada obsahující přírůstkové a kumulativní denní počty provedených PCR testů s korekcí na
    opakovaně pozitivní (kontrolní) testy, a to bez rozdílu způsobu úhrady (tedy včetně samoplátců),
    na COVID 19 za celou ČR podle hlášení laboratoří (rychlotesty nejsou do přehledu zařazeny).
    Tento přehled je k dispozici od 1. srpna 2020 z důvodu úplnosti nahlášených dat jednotlivými
    laboratořemi na individuální úrovni. V předchozím období existuje riziko neúplnosti těchto
    individuálních dat a proto do 31. července vycházíme pouze z dat agregovaných, která však
    neumožňují složitější analytické výpočty.

    Attributes
    ----------

    datum: date

    kraj_nuts_kod: str
        Identifikátor kraje podle klasifikace NUTS 3.

    okres_lau_kod: str
        Identifikátor okresu podle klasifikace LAU 1.

    prirustkovy_pocet_testu_okres: int
        Přírůstkový počet všech provedených testů v daném okrese.

    kumulativni_pocet_testu_okres: int
        Kumulativní počet všech provedených testů v daném okrese.

    prirustkovy_pocet_testu_kraj: int
        Přírůstkový počet všech provedených testů v daném kraji.

    kumulativni_pocet_testu_kraj: int
        Kumulativní počet všech provedených testů v daném kraji.

    prirustkovy_pocet_prvnich_testu_okres: int
        Přírůstkový počet provedených testů s korekcí na opakovaně pozitivní (kontrolní) testy v
        daném okrese.

    kumulativni_pocet_prvnich_testu_okres: int
        Kumulativní počet provedených testů s korekcí na opakovaně pozitivní (kontrolní) testy v
        daném okrese.

    prirustkovy_pocet_prvnich_testu_kraj: int
        Přírůstkový počet provedených testů s korekcí na opakovaně pozitivní (kontrolní) testy v
        daném kraji.

    kumulativni_pocet_prvnich_testu_kraj: int
        Kumulativní počet provedených testů s korekcí na opakovaně pozitivní (kontrolní) testy v
        daném kraji.
    """

    def __init__(self, line: List[str]) :
        self.datum: Optional[date] = date_field(line[0])
        self.kraj_nuts_kod: str = line[1]
        self.okres_lau_kod: str = line[2]
        self.prirustkovy_pocet_testu_okres: int = int_field(line[3])
        self.kumulativni_pocet_testu_okres: int = int_field(line[4])
        self.prirustkovy_pocet_testu_kraj: int = int_field(line[5])
        self.kumulativni_pocet_testu_kraj: int = int_field(line[6])
        self.prirustkovy_pocet_prvnich_testu_okres: int = int_field(line[7])
        self.kumulativni_pocet_prvnich_testu_okres: int = int_field(line[8])
        self.prirustkovy_pocet_prvnich_testu_kraj: int = int_field(line[9])
        self.kumulativni_pocet_prvnich_testu_kraj: int = int_field(line[10])


    @staticmethod
    def get(cache_dir: Optional[str]) -> Iterator['KrajOkresTesty'] :
        return get_many('kraj-okres-testy', KrajOkresTesty, ApiVersion.V2, cache_dir)

