"�A
BHostIDLE"IDLE1     ��@A     ��@a3� t�Q�?i3� t�Q�?�Unknown
�HostResourceApplyAdam""Adam/Adam/update/ResourceApplyAdam(1     Pt@9     Pt@A     Pt@I     Pt@a� 5���?iI��gƴ�?�Unknown
sHost_FusedMatMul"sequential_1/dense_2/Relu(1     �s@9     �s@A     �s@I     �s@a�)��	V�?i|r٣���?�Unknown
�HostResourceApplyAdam"$Adam/Adam/update_2/ResourceApplyAdam(1     @`@9     @`@A     @`@I     @`@a����e��?iQ�(���?�Unknown
}HostMatMul")gradient_tape/sequential_1/dense_2/MatMul(1      _@9      _@A      _@I      _@a�FVQ&�?i��\5��?�Unknown
�HostResourceApplyAdam"$Adam/Adam/update_1/ResourceApplyAdam(1     @\@9     @\@A     @\@I     @\@a��;�V��?il�����?�Unknown
dHostDataset"Iterator::Model(1     �S@9     �S@A     �Q@I     �Q@acڟXǰ�?i?��K>7�?�Unknown
�HostRandomUniform";sequential_1/dropout_1/dropout/random_uniform/RandomUniform(1      H@9      H@A      H@I      H@a�Ј:G��?i��h���?�Unknown
u	HostFlushSummaryWriter"FlushSummaryWriter(1     �@@9     �@@A     �@@I     �@@a|��?i�}���?�Unknown�
^
HostGatherV2"GatherV2(1     �@@9     �@@A     �@@I     �@@a|��?i�^p��?�Unknown
vHost_FusedMatMul"sequential_1/dense_3/BiasAdd(1      6@9      6@A      6@I      6@a[�R�֯t?i}��7�?�Unknown
}HostMatMul")gradient_tape/sequential_1/dense_3/MatMul(1      3@9      3@A      3@I      3@aC����q?iȰy�Z�?�Unknown
HostMatMul"+gradient_tape/sequential_1/dense_3/MatMul_1(1      3@9      3@A      3@I      3@aC����q?i���x~�?�Unknown
�Host#SparseSoftmaxCrossEntropyWithLogits"gsparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits(1      1@9      1@A      1@I      1@a�'�=z�o?i;K�Nq��?�Unknown
�HostDataset"5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat(1      ,@9      ,@A      ,@I      ,@a���n(Tj?i/@/wŸ�?�Unknown
iHostWriteSummary"WriteSummary(1      (@9      (@A      (@I      (@a�Ј:G�f?i �i�V��?�Unknown�
qHostSoftmax"sequential_1/dense_3/Softmax(1      (@9      (@A      (@I      (@a�Ј:G�f?i�Q����?�Unknown
�HostGreaterEqual"+sequential_1/dropout_1/dropout/GreaterEqual(1      (@9      (@A      (@I      (@a�Ј:G�f?i���Ly��?�Unknown
�HostResourceApplyAdam"$Adam/Adam/update_3/ResourceApplyAdam(1      $@9      $@A      $@I      $@a��f�b?iP��G�?�Unknown
�HostMul"Ugradient_tape/sparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/mul(1       @9       @A       @I       @aUa�	^?iۧ�7S�?�Unknown
uHostMul"$sequential_1/dropout_1/dropout/Mul_1(1       @9       @A       @I       @aUa�	^?ifX��^-�?�Unknown
sHostDataset"Iterator::Model::ParallelMapV2(1      @9      @A      @I      @a���n(TZ?i�ҿЈ:�?�Unknown
[HostAddV2"Adam/add(1      @9      @A      @I      @a�Ј:G�V?iH]t�E�?�Unknown
lHostIteratorGetNext"IteratorGetNext(1      @9      @A      @I      @a�Ј:G�V?i�[�Q�?�Unknown
sHostMul""sequential_1/dropout_1/dropout/Mul(1      @9      @A      @I      @a�Ј:G�V?i���b\�?�Unknown
�HostDataset"/Iterator::Model::ParallelMapV2::Zip[0]::FlatMap(1       @9       @A      @I      @a��f�R?io����e�?�Unknown
�HostReluGrad"+gradient_tape/sequential_1/dense_2/ReluGrad(1      @9      @A      @I      @a��f�R?iƼ�!1o�?�Unknown
�HostBiasAddGrad"6gradient_tape/sequential_1/dense_3/BiasAdd/BiasAddGrad(1      @9      @A      @I      @a��f�R?iˠT�x�?�Unknown
tHostAssignAddVariableOp"AssignAddVariableOp(1      @9      @A      @I      @aUa�	N?ic�	��?�Unknown
`HostGatherV2"
GatherV2_1(1      @9      @A      @I      @aUa�	N?i�{r٣��?�Unknown
�HostMul"2gradient_tape/sequential_1/dropout_1/dropout/Mul_2(1      @9      @A      @I      @aUa�	N?i�Sۛ)��?�Unknown
[ HostPow"
Adam/Pow_1(1      @9      @A      @I      @a�Ј:G�F?i#���͔�?�Unknown
Z!HostArgMax"ArgMax(1      @9      @A      @I      @a�Ј:G�F?iW�x?r��?�Unknown
�"HostDataset"?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::TensorSlice(1      @9      @A      @I      @a�Ј:G�F?i�:G���?�Unknown
e#Host
LogicalAnd"
LogicalAnd(1      @9      @A      @I      @a�Ј:G�F?i��㺥�?�Unknown�
�$HostBiasAddGrad"6gradient_tape/sequential_1/dense_2/BiasAdd/BiasAddGrad(1      @9      @A      @I      @a�Ј:G�F?i�~�4_��?�Unknown
u%HostCast"#sequential_1/dropout_1/dropout/Cast(1      @9      @A      @I      @a�Ј:G�F?i'!����?�Unknown
�&HostSum"1sparse_categorical_crossentropy/weighted_loss/Sum(1      @9      @A      @I      @a�Ј:G�F?i[Áا��?�Unknown
~'HostAssignAddVariableOp"Adam/Adam/AssignAddVariableOp(1       @9       @A       @I       @aUa�	>?i~/��j��?�Unknown
](HostCast"Adam/Cast_1(1       @9       @A       @I       @aUa�	>?i���-��?�Unknown
v)HostReadVariableOp"Adam/Cast_2/ReadVariableOp(1       @9       @A       @I       @aUa�	>?i�|���?�Unknown
Y*HostPow"Adam/Pow(1       @9       @A       @I       @aUa�	>?i�sS]���?�Unknown
v+HostAssignAddVariableOp"AssignAddVariableOp_2(1       @9       @A       @I       @aUa�	>?i
��>v��?�Unknown
v,HostAssignAddVariableOp"AssignAddVariableOp_4(1       @9       @A       @I       @aUa�	>?i-L�9��?�Unknown
X-HostEqual"Equal(1       @9       @A       @I       @aUa�	>?iP�� ���?�Unknown
�.HostReadVariableOp"*sequential_1/dense_2/MatMul/ReadVariableOp(1       @9       @A       @I       @aUa�	>?is$%���?�Unknown
�/HostReadVariableOp"*sequential_1/dense_3/MatMul/ReadVariableOp(1       @9       @A       @I       @aUa�	>?i��YÁ��?�Unknown
�0HostCast"`sparse_categorical_crossentropy/ArithmeticOptimizer/ReorderCastLikeAndValuePreserving_float_Cast(1       @9       @A       @I       @aUa�	>?i����D��?�Unknown
�1HostCast"bsparse_categorical_crossentropy/ArithmeticOptimizer/ReorderCastLikeAndValuePreserving_int64_Cast_1(1       @9       @A       @I       @aUa�	>?i�h��?�Unknown
v2HostCast"$sparse_categorical_crossentropy/Cast(1       @9       @A       @I       @aUa�	>?i���f���?�Unknown
t3HostReadVariableOp"Adam/Cast/ReadVariableOp(1      �?9      �?A      �?I      �?aUa�	.?i�׫��?�Unknown
v4HostReadVariableOp"Adam/Cast_3/ReadVariableOp(1      �?9      �?A      �?I      �?aUa�	.?i!A+H���?�Unknown
o5HostReadVariableOp"Adam/ReadVariableOp(1      �?9      �?A      �?I      �?aUa�	.?i2wŸn��?�Unknown
v6HostAssignAddVariableOp"AssignAddVariableOp_1(1      �?9      �?A      �?I      �?aUa�	.?iC�_)P��?�Unknown
v7HostAssignAddVariableOp"AssignAddVariableOp_3(1      �?9      �?A      �?I      �?aUa�	.?iT���1��?�Unknown
X8HostCast"Cast_2(1      �?9      �?A      �?I      �?aUa�	.?ie�
��?�Unknown
X9HostCast"Cast_3(1      �?9      �?A      �?I      �?aUa�	.?ivO.{���?�Unknown
T:HostMul"Mul(1      �?9      �?A      �?I      �?aUa�	.?i�������?�Unknown
V;HostSum"Sum_2(1      �?9      �?A      �?I      �?aUa�	.?i��b\���?�Unknown
w<HostReadVariableOp"div_no_nan/ReadVariableOp_1(1      �?9      �?A      �?I      �?aUa�	.?i���̘��?�Unknown
b=HostDivNoNan"div_no_nan_1(1      �?9      �?A      �?I      �?aUa�	.?i�'�=z��?�Unknown
�>HostMul"0gradient_tape/sequential_1/dropout_1/dropout/Mul(1      �?9      �?A      �?I      �?aUa�	.?i�]1�[��?�Unknown
�?HostReadVariableOp"+sequential_1/dense_2/BiasAdd/ReadVariableOp(1      �?9      �?A      �?I      �?aUa�	.?iܓ�=��?�Unknown
�@HostReadVariableOp"+sequential_1/dense_3/BiasAdd/ReadVariableOp(1      �?9      �?A      �?I      �?aUa�	.?i��e���?�Unknown
�AHostDivNoNan"3sparse_categorical_crossentropy/weighted_loss/value(1      �?9      �?A      �?I      �?aUa�	.?i�������?�Unknown
4BHostIdentity"Identity(i�������?�Unknown�
iCHostDataset"AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensor(i�������?�Unknown
3DHostDivNoNan"
div_no_nan(i�������?�Unknown
HEHostReadVariableOp"div_no_nan/ReadVariableOp(i�������?�Unknown
JFHostReadVariableOp"div_no_nan_1/ReadVariableOp(i�������?�Unknown
LGHostReadVariableOp"div_no_nan_1/ReadVariableOp_1(i�������?�Unknown*�A
�HostResourceApplyAdam""Adam/Adam/update/ResourceApplyAdam(1     Pt@9     Pt@A     Pt@I     Pt@a�&��X��?i�&��X��?�Unknown
sHost_FusedMatMul"sequential_1/dense_2/Relu(1     �s@9     �s@A     �s@I     �s@acX�m_w�?i�� �	�?�Unknown
�HostResourceApplyAdam"$Adam/Adam/update_2/ResourceApplyAdam(1     @`@9     @`@A     @`@I     @`@a��0z�?i�c�P]��?�Unknown
}HostMatMul")gradient_tape/sequential_1/dense_2/MatMul(1      _@9      _@A      _@I      _@a4t:6
յ?i.�j����?�Unknown
�HostResourceApplyAdam"$Adam/Adam/update_1/ResourceApplyAdam(1     @\@9     @\@A     @\@I     @\@a�e9�<�?i���4��?�Unknown
dHostDataset"Iterator::Model(1     �S@9     �S@A     �Q@I     �Q@a�tS%Z �?i/'׫��?�Unknown
�HostRandomUniform";sequential_1/dropout_1/dropout/random_uniform/RandomUniform(1      H@9      H@A      H@I      H@a��ڥ��?i������?�Unknown
uHostFlushSummaryWriter"FlushSummaryWriter(1     �@@9     �@@A     �@@I     �@@a@���=�?ib&��q�?�Unknown�
^	HostGatherV2"GatherV2(1     �@@9     �@@A     �@@I     �@@a@���=�?i̋���*�?�Unknown
v
Host_FusedMatMul"sequential_1/dense_3/BiasAdd(1      6@9      6@A      6@I      6@a �����?ihυ��?�Unknown
}HostMatMul")gradient_tape/sequential_1/dense_3/MatMul(1      3@9      3@A      3@I      3@a�;��Ê?iW8�o��?�Unknown
HostMatMul"+gradient_tape/sequential_1/dense_3/MatMul_1(1      3@9      3@A      3@I      3@a�;��Ê?iF���}�?�Unknown
�Host#SparseSoftmaxCrossEntropyWithLogits"gsparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits(1      1@9      1@A      1@I      1@a���*��?imxfk���?�Unknown
�HostDataset"5Iterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat(1      ,@9      ,@A      ,@I      ,@a�A*��?i�tl�+�?�Unknown
iHostWriteSummary"WriteSummary(1      (@9      (@A      (@I      (@a��ڥ��?i��Fo�?�Unknown�
qHostSoftmax"sequential_1/dense_3/Softmax(1      (@9      (@A      (@I      (@a��ڥ��?iLJ���?�Unknown
�HostGreaterEqual"+sequential_1/dropout_1/dropout/GreaterEqual(1      (@9      (@A      (@I      (@a��ڥ��?i��2~��?�Unknown
�HostResourceApplyAdam"$Adam/Adam/update_3/ResourceApplyAdam(1      $@9      $@A      $@I      $@a�tl�+|?i�[d�.�?�Unknown
�HostMul"Ugradient_tape/sparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/mul(1       @9       @A       @I       @a��#�T�v?i	��[�?�Unknown
uHostMul"$sequential_1/dropout_1/dropout/Mul_1(1       @9       @A       @I       @a��#�T�v?i*з���?�Unknown
sHostDataset"Iterator::Model::ParallelMapV2(1      @9      @A      @I      @a�A*�s?igSk��?�Unknown
[HostAddV2"Adam/add(1      @9      @A      @I      @a��ڥ��p?i�Ϟ9��?�Unknown
lHostIteratorGetNext"IteratorGetNext(1      @9      @A      @I      @a��ڥ��p?i��
��?�Unknown
sHostMul""sequential_1/dropout_1/dropout/Mul(1      @9      @A      @I      @a��ڥ��p?ir:6
��?�Unknown
�HostDataset"/Iterator::Model::ParallelMapV2::Zip[0]::FlatMap(1       @9       @A      @I      @a�tl�+l?i�J� 2�?�Unknown
�HostReluGrad"+gradient_tape/sequential_1/dense_2/ReluGrad(1      @9      @A      @I      @a�tl�+l?i\_^,N�?�Unknown
�HostBiasAddGrad"6gradient_tape/sequential_1/dense_3/BiasAdd/BiasAddGrad(1      @9      @A      @I      @a�tl�+l?i�sXj�?�Unknown
tHostAssignAddVariableOp"AssignAddVariableOp(1      @9      @A      @I      @a��#�T�f?ib�P]��?�Unknown
`HostGatherV2"
GatherV2_1(1      @9      @A      @I      @a��#�T�f?i��-�j��?�Unknown
�HostMul"2gradient_tape/sequential_1/dropout_1/dropout/Mul_2(1      @9      @A      @I      @a��#�T�f?i��
���?�Unknown
[HostPow"
Adam/Pow_1(1      @9      @A      @I      @a��ڥ��`?i1Ű۾�?�Unknown
Z HostArgMax"ArgMax(1      @9      @A      @I      @a��ڥ��`?iޟV���?�Unknown
�!HostDataset"?Iterator::Model::ParallelMapV2::Zip[0]::FlatMap[0]::TensorSlice(1      @9      @A      @I      @a��ڥ��`?i�z����?�Unknown
e"Host
LogicalAnd"
LogicalAnd(1      @9      @A      @I      @a��ڥ��`?i8U����?�Unknown�
�#HostBiasAddGrad"6gradient_tape/sequential_1/dense_2/BiasAdd/BiasAddGrad(1      @9      @A      @I      @a��ڥ��`?i�/Hw�?�Unknown
u$HostCast"#sequential_1/dropout_1/dropout/Cast(1      @9      @A      @I      @a��ڥ��`?i�
�^�?�Unknown
�%HostSum"1sparse_categorical_crossentropy/weighted_loss/Sum(1      @9      @A      @I      @a��ڥ��`?i?�E$�?�Unknown
~&HostAssignAddVariableOp"Adam/Adam/AssignAddVariableOp(1       @9       @A       @I       @a��#�T�V?iw��/�?�Unknown
]'HostCast"Adam/Cast_1(1       @9       @A       @I       @a��#�T�V?i�qY�:�?�Unknown
v(HostReadVariableOp"Adam/Cast_2/ReadVariableOp(1       @9       @A       @I       @a��#�T�V?i���F�?�Unknown
Y)HostPow"Adam/Pow(1       @9       @A       @I       @a��#�T�V?i_,N�WQ�?�Unknown
v*HostAssignAddVariableOp"AssignAddVariableOp_2(1       @9       @A       @I       @a��#�T�V?i'��X�\�?�Unknown
v+HostAssignAddVariableOp"AssignAddVariableOp_4(1       @9       @A       @I       @a��#�T�V?i�O+�g�?�Unknown
X,HostEqual"Equal(1       @9       @A       @I       @a��#�T�V?i�᙭%s�?�Unknown
�-HostReadVariableOp"*sequential_1/dense_2/MatMul/ReadVariableOp(1       @9       @A       @I       @a��#�T�V?isXj~�?�Unknown
�.HostReadVariableOp"*sequential_1/dense_3/MatMul/ReadVariableOp(1       @9       @A       @I       @a��#�T�V?iGw���?�Unknown
�/HostCast"`sparse_categorical_crossentropy/ArithmeticOptimizer/ReorderCastLikeAndValuePreserving_float_Cast(1       @9       @A       @I       @a��#�T�V?i����?�Unknown
�0HostCast"bsparse_categorical_crossentropy/ArithmeticOptimizer/ReorderCastLikeAndValuePreserving_int64_Cast_1(1       @9       @A       @I       @a��#�T�V?i�(TW8��?�Unknown
v1HostCast"$sparse_categorical_crossentropy/Cast(1       @9       @A       @I       @a��#�T�V?i���}��?�Unknown
t2HostReadVariableOp"Adam/Cast/ReadVariableOp(1      �?9      �?A      �?I      �?a��#�T�F?i��V��?�Unknown
v3HostReadVariableOp"Adam/Cast_3/ReadVariableOp(1      �?9      �?A      �?I      �?a��#�T�F?igL1����?�Unknown
o4HostReadVariableOp"Adam/ReadVariableOp(1      �?9      �?A      �?I      �?a��#�T�F?iK�hd��?�Unknown
v5HostAssignAddVariableOp"AssignAddVariableOp_1(1      �?9      �?A      �?I      �?a��#�T�F?i/ޟV��?�Unknown
v6HostAssignAddVariableOp"AssignAddVariableOp_3(1      �?9      �?A      �?I      �?a��#�T�F?i'׫���?�Unknown
X7HostCast"Cast_2(1      �?9      �?A      �?I      �?a��#�T�F?i�oK��?�Unknown
X8HostCast"Cast_3(1      �?9      �?A      �?I      �?a��#�T�F?i۸EV���?�Unknown
T9HostMul"Mul(1      �?9      �?A      �?I      �?a��#�T�F?i�}����?�Unknown
V:HostSum"Sum_2(1      �?9      �?A      �?I      �?a��#�T�F?i�J� 2��?�Unknown
w;HostReadVariableOp"div_no_nan/ReadVariableOp_1(1      �?9      �?A      �?I      �?a��#�T�F?i���U���?�Unknown
b<HostDivNoNan"div_no_nan_1(1      �?9      �?A      �?I      �?a��#�T�F?ik�"�v��?�Unknown
�=HostMul"0gradient_tape/sequential_1/dropout_1/dropout/Mul(1      �?9      �?A      �?I      �?a��#�T�F?iO%Z ��?�Unknown
�>HostReadVariableOp"+sequential_1/dense_2/BiasAdd/ReadVariableOp(1      �?9      �?A      �?I      �?a��#�T�F?i3n�U���?�Unknown
�?HostReadVariableOp"+sequential_1/dense_3/BiasAdd/ReadVariableOp(1      �?9      �?A      �?I      �?a��#�T�F?i�Ȫ]��?�Unknown
�@HostDivNoNan"3sparse_categorical_crossentropy/weighted_loss/value(1      �?9      �?A      �?I      �?a��#�T�F?i�������?�Unknown
4AHostIdentity"Identity(i�������?�Unknown�
iBHostDataset"AIterator::Model::ParallelMapV2::Zip[1]::ForeverRepeat::FromTensor(i�������?�Unknown
3CHostDivNoNan"
div_no_nan(i�������?�Unknown
HDHostReadVariableOp"div_no_nan/ReadVariableOp(i�������?�Unknown
JEHostReadVariableOp"div_no_nan_1/ReadVariableOp(i�������?�Unknown
LFHostReadVariableOp"div_no_nan_1/ReadVariableOp_1(i�������?�Unknown