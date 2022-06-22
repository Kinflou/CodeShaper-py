## System Imports


## Application Imports
from Library.AST.ANtlr.CPP14.Generated.CPP14Parser import CPP14Parser


## Library Imports
from Library.AST.CustomParseTreeVisitor import CustomParseTreeVisitor


class CPP14ParserVisitor(CustomParseTreeVisitor):
    
    def visitErrorNode(self, node):
        pass
    
    @staticmethod
    def visitTranslationUnit(ctx: CPP14Parser.TranslationUnitContext):
        return ctx
    
    @staticmethod
    def visitPrimaryExpression(ctx: CPP14Parser.PrimaryExpressionContext):
        return ctx
    
    @staticmethod
    def visitIdExpression(ctx: CPP14Parser.IdExpressionContext):
        return ctx
    
    @staticmethod
    def visitUnqualifiedId(ctx: CPP14Parser.UnqualifiedIdContext):
        return ctx
    
    @staticmethod
    def visitQualifiedId(ctx: CPP14Parser.QualifiedIdContext):
        return ctx
    
    @staticmethod
    def visitNestedNameSpecifier(ctx: CPP14Parser.NestedNameSpecifierContext):
        return ctx
    
    @staticmethod
    def visitLambdaExpression(ctx: CPP14Parser.LambdaExpressionContext):
        return ctx
    
    @staticmethod
    def visitLambdaIntroducer(ctx: CPP14Parser.LambdaIntroducerContext):
        return ctx
    
    @staticmethod
    def visitLambdaCapture(ctx: CPP14Parser.LambdaCaptureContext):
        return ctx
    
    @staticmethod
    def visitCaptureDefault(ctx: CPP14Parser.CaptureDefaultContext):
        return ctx
    
    @staticmethod
    def visitCaptureList(ctx: CPP14Parser.CaptureListContext):
        return ctx
    
    @staticmethod
    def visitCapture(ctx: CPP14Parser.CaptureContext):
        return ctx
    
    @staticmethod
    def visitSimpleCapture(ctx: CPP14Parser.SimpleCaptureContext):
        return ctx
    
    @staticmethod
    def visitInitcapture(ctx: CPP14Parser.InitcaptureContext):
        return ctx
    
    @staticmethod
    def visitLambdaDeclarator(ctx: CPP14Parser.LambdaDeclaratorContext):
        return ctx
    
    @staticmethod
    def visitPostfixExpression(ctx: CPP14Parser.PostfixExpressionContext):
        return ctx

    
    @staticmethod
    def visitTypeIdOfTheTypeId(ctx: CPP14Parser.TypeIdOfTheTypeIdContext):
        return ctx


    
    @staticmethod
    def visitExpressionList(ctx: CPP14Parser.ExpressionListContext):
        return ctx


    
    @staticmethod
    def visitPseudoDestructorName(ctx: CPP14Parser.PseudoDestructorNameContext):
        return ctx


    # Visit a parse tree produced by CPP14Parser#unaryExpression.
    @staticmethod
    def visitUnaryExpression(ctx: CPP14Parser.UnaryExpressionContext):
        return ctx


    
    @staticmethod
    def visitUnaryOperator(ctx: CPP14Parser.UnaryOperatorContext):
        return ctx


    
    @staticmethod
    def visitNewExpression(ctx: CPP14Parser.NewExpressionContext):
        return ctx


    
    @staticmethod
    def visitNewPlacement(ctx: CPP14Parser.NewPlacementContext):
        return ctx


    
    @staticmethod
    def visitNewTypeId(ctx: CPP14Parser.NewTypeIdContext):
        return ctx


    
    @staticmethod
    def visitNewDeclarator(ctx: CPP14Parser.NewDeclaratorContext):
        return ctx
    
    @staticmethod
    def visitNoPointerNewDeclarator(ctx: CPP14Parser.NoPointerNewDeclaratorContext):
        return ctx
    
    @staticmethod
    def visitNewInitializer(ctx: CPP14Parser.NewInitializerContext):
        return ctx
    
    @staticmethod
    def visitDeleteExpression(ctx: CPP14Parser.DeleteExpressionContext):
        return ctx
    
    @staticmethod
    def visitNoExceptExpression(ctx: CPP14Parser.NoExceptExpressionContext):
        return ctx
    
    @staticmethod
    def visitCastExpression(ctx: CPP14Parser.CastExpressionContext):
        return ctx
    
    @staticmethod
    def visitPointerMemberExpression(ctx: CPP14Parser.PointerMemberExpressionContext):
        return ctx
    
    @staticmethod
    def visitMultiplicativeExpression(ctx: CPP14Parser.MultiplicativeExpressionContext):
        return ctx
    
    @staticmethod
    def visitAdditiveExpression(ctx: CPP14Parser.AdditiveExpressionContext):
        return ctx
    
    @staticmethod
    def visitShiftExpression(ctx: CPP14Parser.ShiftExpressionContext):
        return ctx
    
    @staticmethod
    def visitShiftOperator(ctx: CPP14Parser.ShiftOperatorContext):
        return ctx
    
    @staticmethod
    def visitRelationalExpression(ctx: CPP14Parser.RelationalExpressionContext):
        return ctx
    
    @staticmethod
    def visitEqualityExpression(ctx: CPP14Parser.EqualityExpressionContext):
        return ctx
    
    @staticmethod
    def visitAndExpression(ctx: CPP14Parser.AndExpressionContext):
        return ctx
    
    @staticmethod
    def visitExclusiveOrExpression(ctx: CPP14Parser.ExclusiveOrExpressionContext):
        return ctx
    
    @staticmethod
    def visitInclusiveOrExpression(ctx: CPP14Parser.InclusiveOrExpressionContext):
        return ctx
    
    @staticmethod
    def visitLogicalAndExpression(ctx: CPP14Parser.LogicalAndExpressionContext):
        return ctx
    
    @staticmethod
    def visitLogicalOrExpression(ctx: CPP14Parser.LogicalOrExpressionContext):
        return ctx
    
    @staticmethod
    def visitConditionalExpression(ctx: CPP14Parser.ConditionalExpressionContext):
        return ctx
    
    @staticmethod
    def visitAssignmentExpression(ctx: CPP14Parser.AssignmentExpressionContext):
        return ctx
    
    @staticmethod
    def visitAssignmentOperator(ctx: CPP14Parser.AssignmentOperatorContext):
        return ctx
    
    @staticmethod
    def visitExpression(ctx: CPP14Parser.ExpressionContext):
        return ctx
    
    @staticmethod
    def visitConstantExpression(ctx: CPP14Parser.ConstantExpressionContext):
        return ctx
    
    @staticmethod
    def visitStatement(ctx: CPP14Parser.StatementContext):
        return ctx
    
    @staticmethod
    def visitLabeledStatement(ctx: CPP14Parser.LabeledStatementContext):
        return ctx
    
    @staticmethod
    def visitExpressionStatement(ctx: CPP14Parser.ExpressionStatementContext):
        return ctx
    
    @staticmethod
    def visitCompoundStatement(ctx: CPP14Parser.CompoundStatementContext):
        return ctx
    
    @staticmethod
    def visitStatementSeq(ctx: CPP14Parser.StatementSeqContext):
        return ctx
    
    @staticmethod
    def visitSelectionStatement(ctx: CPP14Parser.SelectionStatementContext):
        return ctx
    
    @staticmethod
    def visitCondition(ctx: CPP14Parser.ConditionContext):
        return ctx
    
    @staticmethod
    def visitIterationStatement(ctx: CPP14Parser.IterationStatementContext):
        return ctx
    
    @staticmethod
    def visitForInitStatement(ctx: CPP14Parser.ForInitStatementContext):
        return ctx
    
    @staticmethod
    def visitForRangeDeclaration(ctx: CPP14Parser.ForRangeDeclarationContext):
        return ctx
    
    @staticmethod
    def visitForRangeInitializer(ctx: CPP14Parser.ForRangeInitializerContext):
        return ctx
    
    @staticmethod
    def visitJumpStatement(ctx: CPP14Parser.JumpStatementContext):
        return ctx
    
    @staticmethod
    def visitDeclarationStatement(ctx: CPP14Parser.DeclarationStatementContext):
        return ctx
    
    @staticmethod
    def visitDeclarationseq(ctx: CPP14Parser.DeclarationseqContext):
        return ctx
    
    @staticmethod
    def visitDeclaration(ctx: CPP14Parser.DeclarationContext):
        return ctx
    
    @staticmethod
    def visitBlockDeclaration(ctx: CPP14Parser.BlockDeclarationContext):
        return ctx
    
    @staticmethod
    def visitAliasDeclaration(ctx: CPP14Parser.AliasDeclarationContext):
        return ctx
    
    @staticmethod
    def visitSimpleDeclaration(ctx: CPP14Parser.SimpleDeclarationContext):
        return ctx
    
    @staticmethod
    def visitStaticAssertDeclaration(ctx: CPP14Parser.StaticAssertDeclarationContext):
        return ctx
    
    @staticmethod
    def visitEmptyDeclaration(ctx: CPP14Parser.EmptyDeclarationContext):
        return ctx
    
    @staticmethod
    def visitAttributeDeclaration(ctx: CPP14Parser.AttributeDeclarationContext):
        return ctx
    
    @staticmethod
    def visitDeclSpecifier(ctx: CPP14Parser.DeclSpecifierContext):
        return ctx
    
    @staticmethod
    def visitDeclSpecifierSeq(ctx: CPP14Parser.DeclSpecifierSeqContext):
        return ctx
    
    @staticmethod
    def visitStorageClassSpecifier(ctx: CPP14Parser.StorageClassSpecifierContext):
        return ctx
    
    @staticmethod
    def visitFunctionSpecifier(ctx: CPP14Parser.FunctionSpecifierContext):
        return ctx
    
    @staticmethod
    def visitTypedefName(ctx: CPP14Parser.TypedefNameContext):
        return ctx


    
    @staticmethod
    def visitTypeSpecifier(ctx: CPP14Parser.TypeSpecifierContext):
        return ctx


    
    @staticmethod
    def visitTrailingTypeSpecifier(ctx: CPP14Parser.TrailingTypeSpecifierContext):
        return ctx


    
    @staticmethod
    def visitTypeSpecifierSeq(ctx: CPP14Parser.TypeSpecifierSeqContext):
        return ctx


    
    @staticmethod
    def visitTrailingTypeSpecifierSeq(ctx: CPP14Parser.TrailingTypeSpecifierSeqContext):
        return ctx


    
    @staticmethod
    def visitSimpleTypeLengthModifier(ctx: CPP14Parser.SimpleTypeLengthModifierContext):
        return ctx


    
    @staticmethod
    def visitSimpleTypeSignednessModifier(ctx: CPP14Parser.SimpleTypeSignednessModifierContext):
        return ctx


    
    @staticmethod
    def visitSimpleTypeSpecifier(ctx: CPP14Parser.SimpleTypeSpecifierContext):
        return ctx


    
    @staticmethod
    def visitTheTypeName(ctx: CPP14Parser.TheTypeNameContext):
        return ctx


    
    @staticmethod
    def visitDecltypeSpecifier(ctx: CPP14Parser.DecltypeSpecifierContext):
        return ctx


    
    @staticmethod
    def visitElaboratedTypeSpecifier(ctx: CPP14Parser.ElaboratedTypeSpecifierContext):
        return ctx


    
    @staticmethod
    def visitEnumName(ctx: CPP14Parser.EnumNameContext):
        return ctx


    
    @staticmethod
    def visitEnumSpecifier(ctx: CPP14Parser.EnumSpecifierContext):
        return ctx


    
    @staticmethod
    def visitEnumHead(ctx: CPP14Parser.EnumHeadContext):
        return ctx


    
    @staticmethod
    def visitOpaqueEnumDeclaration(ctx: CPP14Parser.OpaqueEnumDeclarationContext):
        return ctx


    
    @staticmethod
    def visitEnumkey(ctx: CPP14Parser.EnumkeyContext):
        return ctx


    
    @staticmethod
    def visitEnumbase(ctx: CPP14Parser.EnumbaseContext):
        return ctx


    
    @staticmethod
    def visitEnumeratorList(ctx: CPP14Parser.EnumeratorListContext):
        return ctx


    
    @staticmethod
    def visitEnumeratorDefinition(ctx: CPP14Parser.EnumeratorDefinitionContext):
        return ctx


    
    @staticmethod
    def visitEnumerator(ctx: CPP14Parser.EnumeratorContext):
        return ctx


    
    @staticmethod
    def visitNamespaceName(ctx: CPP14Parser.NamespaceNameContext):
        return ctx


    
    @staticmethod
    def visitOriginalNamespaceName(ctx: CPP14Parser.OriginalNamespaceNameContext):
        return ctx


    
    @staticmethod
    def visitNamespaceDefinition(ctx: CPP14Parser.NamespaceDefinitionContext):
        return ctx


    
    @staticmethod
    def visitNamespaceAlias(ctx: CPP14Parser.NamespaceAliasContext):
        return ctx


    
    @staticmethod
    def visitNamespaceAliasDefinition(ctx: CPP14Parser.NamespaceAliasDefinitionContext):
        return ctx


    
    @staticmethod
    def visitQualifiednamespacespecifier(ctx: CPP14Parser.QualifiednamespacespecifierContext):
        return ctx


    
    @staticmethod
    def visitUsingDeclaration(ctx: CPP14Parser.UsingDeclarationContext):
        return ctx


    
    @staticmethod
    def visitUsingDirective(ctx: CPP14Parser.UsingDirectiveContext):
        return ctx


    
    @staticmethod
    def visitAsmDefinition(ctx: CPP14Parser.AsmDefinitionContext):
        return ctx


    
    @staticmethod
    def visitLinkageSpecification(ctx: CPP14Parser.LinkageSpecificationContext):
        return ctx


    
    @staticmethod
    def visitAttributeSpecifierSeq(ctx: CPP14Parser.AttributeSpecifierSeqContext):
        return ctx


    
    @staticmethod
    def visitAttributeSpecifier(ctx: CPP14Parser.AttributeSpecifierContext):
        return ctx


    
    @staticmethod
    def visitAlignmentspecifier(ctx: CPP14Parser.AlignmentspecifierContext):
        return ctx


    
    @staticmethod
    def visitAttributeList(ctx: CPP14Parser.AttributeListContext):
        return ctx


    
    @staticmethod
    def visitAttribute(ctx: CPP14Parser.AttributeContext):
        return ctx


    
    @staticmethod
    def visitAttributeNamespace(ctx: CPP14Parser.AttributeNamespaceContext):
        return ctx


    
    @staticmethod
    def visitAttributeArgumentClause(ctx: CPP14Parser.AttributeArgumentClauseContext):
        return ctx


    
    @staticmethod
    def visitBalancedTokenSeq(ctx: CPP14Parser.BalancedTokenSeqContext):
        return ctx


    
    @staticmethod
    def visitBalancedtoken(ctx: CPP14Parser.BalancedtokenContext):
        return ctx


    
    @staticmethod
    def visitInitDeclaratorList(ctx: CPP14Parser.InitDeclaratorListContext):
        return ctx


    
    @staticmethod
    def visitInitDeclarator(ctx: CPP14Parser.InitDeclaratorContext):
        return ctx


    
    @staticmethod
    def visitDeclarator(ctx: CPP14Parser.DeclaratorContext):
        return ctx


    
    @staticmethod
    def visitPointerDeclarator(ctx: CPP14Parser.PointerDeclaratorContext):
        return ctx


    
    @staticmethod
    def visitNoPointerDeclarator(ctx: CPP14Parser.NoPointerDeclaratorContext):
        return ctx


    
    @staticmethod
    def visitParametersAndQualifiers(ctx: CPP14Parser.ParametersAndQualifiersContext):
        return ctx


    
    @staticmethod
    def visitTrailingReturnType(ctx: CPP14Parser.TrailingReturnTypeContext):
        return ctx


    
    @staticmethod
    def visitPointerOperator(ctx: CPP14Parser.PointerOperatorContext):
        return ctx


    
    @staticmethod
    def visitCvqualifierseq(ctx: CPP14Parser.CvqualifierseqContext):
        return ctx


    
    @staticmethod
    def visitCvQualifier(ctx: CPP14Parser.CvQualifierContext):
        return ctx


    
    @staticmethod
    def visitRefqualifier(ctx: CPP14Parser.RefqualifierContext):
        return ctx


    
    @staticmethod
    def visitDeclaratorid(ctx: CPP14Parser.DeclaratoridContext):
        return ctx


    
    @staticmethod
    def visitTheTypeId(ctx: CPP14Parser.TheTypeIdContext):
        return ctx


    
    @staticmethod
    def visitAbstractDeclarator(ctx: CPP14Parser.AbstractDeclaratorContext):
        return ctx


    
    @staticmethod
    def visitPointerAbstractDeclarator(ctx: CPP14Parser.PointerAbstractDeclaratorContext):
        return ctx


    
    @staticmethod
    def visitNoPointerAbstractDeclarator(ctx: CPP14Parser.NoPointerAbstractDeclaratorContext):
        return ctx
    
    @staticmethod
    def visitAbstractPackDeclarator(ctx: CPP14Parser.AbstractPackDeclaratorContext):
        return ctx
    
    @staticmethod
    def visitNoPointerAbstractPackDeclarator(ctx: CPP14Parser.NoPointerAbstractPackDeclaratorContext):
        return ctx
    
    @staticmethod
    def visitParameterDeclarationClause(ctx: CPP14Parser.ParameterDeclarationClauseContext):
        return ctx
    
    @staticmethod
    def visitParameterDeclarationList(ctx: CPP14Parser.ParameterDeclarationListContext):
        return ctx
    
    @staticmethod
    def visitParameterDeclaration(ctx: CPP14Parser.ParameterDeclarationContext):
        return ctx
    
    @staticmethod
    def visitFunctionDefinition(ctx: CPP14Parser.FunctionDefinitionContext):
        return ctx
    
    @staticmethod
    def visitFunctionBody(ctx: CPP14Parser.FunctionBodyContext):
        return ctx
    
    @staticmethod
    def visitInitializer(ctx: CPP14Parser.InitializerContext):
        return ctx
    
    
    @staticmethod
    def visitBraceOrEqualInitializer(ctx: CPP14Parser.BraceOrEqualInitializerContext):
        return ctx


    
    @staticmethod
    def visitInitializerClause(ctx: CPP14Parser.InitializerClauseContext):
        return ctx


    
    @staticmethod
    def visitInitializerList(ctx: CPP14Parser.InitializerListContext):
        return ctx


    
    @staticmethod
    def visitBracedInitList(ctx: CPP14Parser.BracedInitListContext):
        return ctx


    
    @staticmethod
    def visitClassName(ctx: CPP14Parser.ClassNameContext):
        return ctx


    
    @staticmethod
    def visitClassSpecifier(ctx: CPP14Parser.ClassSpecifierContext):
        return ctx


    
    @staticmethod
    def visitClassHead(ctx: CPP14Parser.ClassHeadContext):
        return ctx


    
    @staticmethod
    def visitClassHeadName(ctx: CPP14Parser.ClassHeadNameContext):
        return ctx


    
    @staticmethod
    def visitClassVirtSpecifier(ctx: CPP14Parser.ClassVirtSpecifierContext):
        return ctx


    
    @staticmethod
    def visitClassKey(ctx: CPP14Parser.ClassKeyContext):
        return ctx


    
    @staticmethod
    def visitMemberSpecification(ctx: CPP14Parser.MemberSpecificationContext):
        return ctx


    
    @staticmethod
    def visitMemberdeclaration(ctx: CPP14Parser.MemberdeclarationContext):
        return ctx


    
    @staticmethod
    def visitMemberDeclaratorList(ctx: CPP14Parser.MemberDeclaratorListContext):
        return ctx


    
    @staticmethod
    def visitMemberDeclarator(ctx: CPP14Parser.MemberDeclaratorContext):
        return ctx


    
    @staticmethod
    def visitVirtualSpecifierSeq(ctx: CPP14Parser.VirtualSpecifierSeqContext):
        return ctx


    
    @staticmethod
    def visitVirtualSpecifier(ctx: CPP14Parser.VirtualSpecifierContext):
        return ctx


    
    @staticmethod
    def visitPureSpecifier(ctx: CPP14Parser.PureSpecifierContext):
        return ctx


    
    @staticmethod
    def visitBaseClause(ctx: CPP14Parser.BaseClauseContext):
        return ctx


    
    @staticmethod
    def visitBaseSpecifierList(ctx: CPP14Parser.BaseSpecifierListContext):
        return ctx


    
    @staticmethod
    def visitBaseSpecifier(ctx: CPP14Parser.BaseSpecifierContext):
        return ctx


    
    @staticmethod
    def visitClassOrDeclType(ctx: CPP14Parser.ClassOrDeclTypeContext):
        return ctx


    
    @staticmethod
    def visitBaseTypeSpecifier(ctx: CPP14Parser.BaseTypeSpecifierContext):
        return ctx


    
    @staticmethod
    def visitAccessSpecifier(ctx: CPP14Parser.AccessSpecifierContext):
        return ctx


    
    @staticmethod
    def visitConversionFunctionId(ctx: CPP14Parser.ConversionFunctionIdContext):
        return ctx


    
    @staticmethod
    def visitConversionTypeId(ctx: CPP14Parser.ConversionTypeIdContext):
        return ctx


    
    @staticmethod
    def visitConversionDeclarator(ctx: CPP14Parser.ConversionDeclaratorContext):
        return ctx


    
    @staticmethod
    def visitConstructorInitializer(ctx: CPP14Parser.ConstructorInitializerContext):
        return ctx


    
    @staticmethod
    def visitMemInitializerList(ctx: CPP14Parser.MemInitializerListContext):
        return ctx


    
    @staticmethod
    def visitMemInitializer(ctx: CPP14Parser.MemInitializerContext):
        return ctx


    
    @staticmethod
    def visitMeminitializerid(ctx: CPP14Parser.MeminitializeridContext):
        return ctx


    
    @staticmethod
    def visitOperatorFunctionId(ctx: CPP14Parser.OperatorFunctionIdContext):
        return ctx


    
    @staticmethod
    def visitLiteralOperatorId(ctx: CPP14Parser.LiteralOperatorIdContext):
        return ctx


    
    @staticmethod
    def visitTemplateDeclaration(ctx: CPP14Parser.TemplateDeclarationContext):
        return ctx


    
    @staticmethod
    def visitTemplateparameterList(ctx: CPP14Parser.TemplateparameterListContext):
        return ctx


    
    @staticmethod
    def visitTemplateParameter(ctx: CPP14Parser.TemplateParameterContext):
        return ctx


    
    @staticmethod
    def visitTypeParameter(ctx: CPP14Parser.TypeParameterContext):
        return ctx


    
    @staticmethod
    def visitSimpleTemplateId(ctx: CPP14Parser.SimpleTemplateIdContext):
        return ctx


    
    @staticmethod
    def visitTemplateId(ctx: CPP14Parser.TemplateIdContext):
        return ctx


    
    @staticmethod
    def visitTemplateName(ctx: CPP14Parser.TemplateNameContext):
        return ctx


    
    @staticmethod
    def visitTemplateArgumentList(ctx: CPP14Parser.TemplateArgumentListContext):
        return ctx


    
    @staticmethod
    def visitTemplateArgument(ctx: CPP14Parser.TemplateArgumentContext):
        return ctx


    
    @staticmethod
    def visitTypeNameSpecifier(ctx: CPP14Parser.TypeNameSpecifierContext):
        return ctx


    
    @staticmethod
    def visitExplicitInstantiation(ctx: CPP14Parser.ExplicitInstantiationContext):
        return ctx
    
    
    @staticmethod
    def visitExplicitSpecialization(ctx: CPP14Parser.ExplicitSpecializationContext):
        return ctx
    
    @staticmethod
    def visitTryBlock(ctx: CPP14Parser.TryBlockContext):
        return ctx
    
    @staticmethod
    def visitFunctionTryBlock(ctx: CPP14Parser.FunctionTryBlockContext):
        return ctx
    
    
    @staticmethod
    def visitHandlerSeq(ctx: CPP14Parser.HandlerSeqContext):
        return ctx
    
    
    @staticmethod
    def visitHandler(ctx: CPP14Parser.HandlerContext):
        return ctx


    
    @staticmethod
    def visitExceptionDeclaration(ctx: CPP14Parser.ExceptionDeclarationContext):
        return ctx

    @staticmethod
    def visitThrowExpression(ctx: CPP14Parser.ThrowExpressionContext):
        return ctx
    
    @staticmethod
    def visitExceptionSpecification(ctx: CPP14Parser.ExceptionSpecificationContext):
        return ctx
    
    @staticmethod
    def visitDynamicExceptionSpecification(ctx: CPP14Parser.DynamicExceptionSpecificationContext):
        return ctx
    
    @staticmethod
    def visitTypeIdList(ctx: CPP14Parser.TypeIdListContext):
        return ctx
    
    @staticmethod
    def visitNoeExceptSpecification(ctx: CPP14Parser.NoeExceptSpecificationContext):
        return ctx
    
    @staticmethod
    def visitTheOperator(ctx: CPP14Parser.TheOperatorContext):
        return ctx
    
    @staticmethod
    def visitLiteral(ctx: CPP14Parser.LiteralContext):
        return ctx


del CPP14Parser
