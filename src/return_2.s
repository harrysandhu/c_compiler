	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 10, 15	sdk_version 10, 15, 6
	.globl	_main                   ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
## %bb.0:
	pushq	%rbp
	movq	%rsp, %rbp  
	movl	$2, %eax    				## move constant 2 into eax reg
	popq	%rbp
	retq
                                        ## -- End function

.subsections_via_symbols